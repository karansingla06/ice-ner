import traceback
import torch, time, sys, argparse, os, codecs, h5py, csv
import pickle
import numpy as np
from torch.autograd import Variable
from nltk import ParentedTree
from train_scpn import SCPN
from train_parse_generator import ParseNet
from subwordnmt.apply_bpe import BPE, read_vocabulary
from scpn_utils import deleaf, parse_indexify_transformations
import re
import os
from stanfordcorenlp import StanfordCoreNLP
import spacy
from benepar.spacy_plugin import BeneparComponent
from variation_conf_settings import cparser_flag
from importlib import reload
import logging
reload(sys)
#sys.setdefaultencoding('utf8')
logger = logging.getLogger(__name__)

logger.info("if cuda is available-- ", torch.cuda.is_available())

# 10 frequent templates


templates = [
    '( ROOT ( S ( NP ) ( VP ) ( . ) ) ) EOP',
    '( ROOT ( S ( VP ) ( . ) ) ) EOP',
    '( ROOT ( NP ( NP ) ( . ) ) ) EOP',
    '( ROOT ( FRAG ( SBAR ) ( . ) ) ) EOP',
    '( ROOT ( S ( S ) ( , ) ( CC ) ( S ) ( . ) ) ) EOP',
    '( ROOT ( S ( LST ) ( VP ) ( . ) ) ) EOP',
    '( ROOT ( SBARQ ( WHADVP ) ( SQ ) ( . ) ) ) EOP',
    '( ROOT ( S ( PP ) ( , ) ( NP ) ( VP ) ( . ) ) ) EOP',
    '( ROOT ( S ( ADVP ) ( NP ) ( VP ) ( . ) ) ) EOP',
    '( ROOT ( S ( SBAR ) ( , ) ( NP ) ( VP ) ( . ) ) ) EOP'
]


### loading all initial models and preprocessing
#print os.getcwd()+"/stanford-corenlp-full-2017-06-09" 
#cparser_flag=1
if cparser_flag == 1:
   nlp = spacy.load('en')
   nlp.add_pipe(BeneparComponent("benepar_en2"))
else:
   nlp = StanfordCoreNLP(os.getcwd()+"/stanford-corenlp-full-2018-10-05" )
gpu ='0'
vocab = './data/parse_vocab.pkl'
parse_vocab = './data/ptb_tagset.txt'
pp_model = "./models/scpn.pt"
parse_model = "models/parse_generator.pt"
    ## BPE args
bpe_codes= 'data/bpe.codes'
    # parser.add_argument('--bpe_vocab', type=str, default='data/vocab.txt')
bpe_vocab = 'data/vocab.txt'
    # parser.add_argument('--bpe_vocab_thresh', type=int, default=50)
bpe_vocab_thresh = 50
os.environ['CUDA_VISIBLE_DEVICES'] = gpu
    # load saved models
pp_model = torch.load(pp_model)

parse_model = torch.load(parse_model)
    # load vocab
pp_vocab, rev_pp_vocab = pickle.load(open(vocab, 'rb'))



tag_file = codecs.open(parse_vocab, 'r', 'utf-8')
parse_gen_voc = {}
for idx, line in enumerate(tag_file):
    line = line.strip()
    parse_gen_voc[line] = idx
rev_label_voc = dict((v, k) for (k, v) in parse_gen_voc.items())

    # load paraphrase network
pp_args = pp_model['config_args']
net = SCPN(pp_args.d_word, pp_args.d_hid, pp_args.d_nt, pp_args.d_trans,
           len(pp_vocab), len(parse_gen_voc) - 1, pp_args.use_input_parse)
net.cuda()
net.load_state_dict(pp_model['state_dict'])
net.eval()
    # load parse generator network
parse_args = parse_model['config_args']
parse_net = ParseNet(parse_args.d_nt, parse_args.d_hid, len(parse_gen_voc))
parse_net.cuda()
parse_net.load_state_dict(parse_model['state_dict'])
parse_net.eval()
    # encode templates
template_lens = [len(x.split()) for x in templates]
np_templates = np.zeros((len(templates), max(template_lens)), dtype='int32')
for z, template in enumerate(templates):
    np_templates[z, :template_lens[z]] = [parse_gen_voc[w] for w in templates[z].split()]
tp_templates = Variable(torch.from_numpy(np_templates).long().cuda())
tp_template_lens = torch.from_numpy(np.array(template_lens, dtype='int32')).long().cuda()

    # instantiate BPE segmenter
bpe_codes = codecs.open(bpe_codes, encoding='utf-8')
bpe_vocab = codecs.open(bpe_vocab, encoding='utf-8')
bpe_vocab = read_vocabulary(bpe_vocab, bpe_vocab_thresh)
bpe = BPE(bpe_codes, '@@', bpe_vocab, None)


def reverse_bpe(sent):
    x = []
    cache = ''

    for w in sent:
        if w.endswith('@@'):
            cache += w.replace('@@', '')
        elif cache != '':
            x.append(cache + w)
            cache = ''
        else:
            x.append(w)

    return ' '.join(x)


# encode sentences and parses for targeted paraphrasing

def encode_data(text, parsed_repr, bpe, pp_vocab, parse_gen_voc,parse_net,tp_templates,tp_template_lens, net, rev_label_voc, rev_pp_vocab):
    stime = time.time()
    ssent = ' '.join(text.split())
    seg_sent = bpe.segment(ssent.lower()).split()

    results = []

    results.append(reverse_bpe(seg_sent))
    # encode sentence using pp_vocab, leave one word for EOS
    seg_sent = [pp_vocab[w] for w in seg_sent if w in pp_vocab]

    # add EOS
    seg_sent.append(pp_vocab['EOS'])
    torch_sent = Variable(torch.from_numpy(np.array(seg_sent, dtype='int32')).long().cuda())
    torch_sent_len = torch.from_numpy(np.array([len(seg_sent)], dtype='int32')).long().cuda()

    # encode parse using parse vocab
    parse_tree = ParentedTree.fromstring(parsed_repr.strip())
    parse_tree = deleaf(parse_tree)
    np_parse = np.array([parse_gen_voc[w] for w in parse_tree], dtype='int32')
    torch_parse = Variable(torch.from_numpy(np_parse).long().cuda())
    torch_parse_len = torch.from_numpy(np.array([len(parse_tree)], dtype='int32')).long().cuda()

    # generate full parses from templates
    beam_dict = parse_net.batch_beam_search(torch_parse.unsqueeze(0), tp_templates,
                                            torch_parse_len[:], tp_template_lens, parse_gen_voc['EOP'], beam_size=3,
                                            max_steps=150)
    seq_lens = []
    seqs = []
    for b_idx in beam_dict:
        prob, _, _, seq = beam_dict[b_idx][0]
        seq = seq[:-1]  # chop off EOP
        seq_lens.append(len(seq))
        seqs.append(seq)
    np_parses = np.zeros((len(seqs), max(seq_lens)), dtype='int32')
    for z, seq in enumerate(seqs):
        np_parses[z, :seq_lens[z]] = seq
    tp_parses = Variable(torch.from_numpy(np_parses).long().cuda())
    tp_len = torch.from_numpy(np.array(seq_lens, dtype='int32')).long().cuda()

    # generate paraphrases from parses
    try:
        beam_dict = net.batch_beam_search(torch_sent.unsqueeze(0), tp_parses,
                                          torch_sent_len[:], tp_len, pp_vocab['EOS'], beam_size=3, max_steps=40)
        for b_idx in beam_dict:
            prob, _, _, seq = beam_dict[b_idx][0]
            gen_parse = ' '.join([rev_label_voc[z] for z in seqs[b_idx]])
            gen_sent = ' '.join([rev_pp_vocab[w] for w in seq[:-1]])
            results.append(reverse_bpe(gen_sent.split()))
    except:
        print("beam search OOM")
        print(traceback.format_exc())
    return results


def generate_variations(text):
    try:
        print(text)
        if cparser_flag==1:
           if not isinstance(text, str):
              text = str(text,'utf-8')
           doc = nlp(text)
           sent = list(doc.sents)[0]
           parsed_repr = sent._.parse_string
        else:
           parsed_repr = re.sub(' +', ' ', str(nlp.parse(text).replace("\n", "")))


        # parser = argparse.ArgumentParser(description='Syntactically Controlled Paraphrase Transformer')
        description = 'Syntactically Controlled Paraphrase Transformer'
        # paraphrase the sst!
        res= encode_data(text, parsed_repr,bpe,pp_vocab, parse_gen_voc,parse_net, tp_templates,tp_template_lens, net, rev_label_voc, rev_pp_vocab)
        return res
    except:
        logger.info(traceback.format_exc())


#
#if __name__=="__main__":
 #    print('----------------------starting -------------------------- ')
  #   print(generate_variations("A quick lazy fox jumps over the dog"))
