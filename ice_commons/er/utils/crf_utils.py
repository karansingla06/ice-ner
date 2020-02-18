import re
import logging
from ice_commons.store.models import ModelStore
model_store=ModelStore()

logger = logging.getLogger(__name__)

def pos_tags_predict(text,original_text, language):
    tokens = model_store.get_pos_tags(text, original_text, language)
    text_tokens = text.split()
    logger.info("pos_tags_predict %s" %text)
    logger.info("pos_tags_predict %s" % original_text)
    tags = []
    for ind, tok in enumerate(tokens):
        tags.append((text_tokens[ind],tok.get("pos"),tok.get("lemma")))
    return tags

def pos_tags_train(text,original_text, language):
    tokens = model_store.get_pos_tags(text, original_text, language)
    tags = []
    for tok in tokens:
        tags.append((tok.get("text"),tok.get("pos"),tok.get("lemma")))
    return tags

def get_type(token):
    T = (
        'AllUpper', 'AllDigit', 'AllSymbol',
        'AllUpperDigit', 'AllUpperSymbol', 'AllDigitSymbol',
        'AllUpperDigitSymbol',
        'InitUpper',
        'AllLetter',
        'AllAlnum',
    )
    R = set(T)
    if not token:
        return 'EMPTY'

    for i in range(len(token)):
        c = token[i]
        if c.isupper():
            R.discard('AllDigit')
            R.discard('AllSymbol')
            R.discard('AllDigitSymbol')
        elif c.isdigit() or c in (',', '.'):
            R.discard('AllUpper')
            R.discard('AllSymbol')
            R.discard('AllUpperSymbol')
            R.discard('AllLetter')
        elif c.islower():
            R.discard('AllUpper')
            R.discard('AllDigit')
            R.discard('AllSymbol')
            R.discard('AllUpperDigit')
            R.discard('AllUpperSymbol')
            R.discard('AllDigitSymbol')
            R.discard('AllUpperDigitSymbol')
        else:
            R.discard('AllUpper')
            R.discard('AllDigit')
            R.discard('AllUpperDigit')
            R.discard('AllLetter')
            R.discard('AllAlnum')

        if i == 0 and not c.isupper():
            R.discard('InitUpper')

    for tag in T:
        if tag in R:
            return tag
    return 'NO'


### if the first letter is uppercase
def get_cap(token):
    if token[0].isupper():
        return "T"
    else:
        return "F"


### 2 digits
def get_2d(token):
    return len(token) == 2 and token.isdigit()


### 4 digits
def get_4d(token):
    return len(token) == 4 and token.isdigit()


### contains only digits and alpha
def get_da(token):
    bd = False
    ba = False
    for c in token:
        if c.isdigit():
            bd = True
        elif c.isalpha():
            ba = True
        else:
            return False
    return bd and ba


### contains only digits and symbol-p
def get_dand(token, p):
    bd = False
    bdd = False
    for c in token:
        if c.isdigit():
            bd = True
        elif c == p:
            bdd = True
        else:
            return False
    return bd and bdd


### contains only digits and symbol-
def get_dandhyp(token, p='-'):
    bd = False
    bdd = False
    for c in token:
        if c.isdigit():
            bd = True
        elif c == p:
            bdd = True
        else:
            return False
    return bd and bdd


def get_dandsls(token, p='/'):
    bd = False
    bdd = False
    for c in token:
        if c.isdigit():
            bd = True
        elif c == p or c == "\/":
            bdd = True
        else:
            return False
    return bd and bdd


### all chars are neither alphabet nor digits
def get_all_other(token):
    for c in token:
        if c.isalnum():
            return False
    return True


### Cap + "."
def get_capperiod(token):
    return len(token) == 2 and token[0].isupper() and token[1] == '.'


### contains capital letter
def contains_upper(token):
    b = False
    for c in token:
        b |= c.isupper()
    return b


### contains lowercase letter
def contains_lower(token):
    b = False
    for c in token:
        b |= c.islower()
    return b


### contains alphabet
def contains_alpha(token):
    b = False
    for c in token:
        b |= c.isalpha()
    return b


### contains digit
def contains_digit(token):
    b = False
    for c in token:
        b |= c.isdigit()
    return b


def get_hyp(token):
    if '-' in token:
        return True
    else:
        return False


def get_dollar(token):
    if '$' in token:
        return True
    else:
        return False


def get_shape(word):
    word_shape = 'other'
    if re.match('[0-9]+(\.[0-9]*)?|[0-9]*\.[0-9]+$', word):
        word_shape = 'number'
    elif re.match('\W+$', word):
        word_shape = 'punct'
    elif re.match('[A-Z][a-z]+$', word):
        word_shape = 'capitalized'
    elif re.match('[A-Z]+$', word):
        word_shape = 'uppercase'
    elif re.match('[a-z]+$', word):
        word_shape = 'lowercase'
    elif re.match('[A-Z][a-z]+[A-Z][a-z]+[A-Za-z]*$', word):
        word_shape = 'camelcase'
    elif re.match('[A-Za-z]+$', word):
        word_shape = 'mixedcase'
    elif re.match('__.+__$', word):
        word_shape = 'wildcard'
    elif re.match('[A-Za-z0-9]+\.$', word):
        word_shape = 'ending-dot'
    elif re.match('[A-Za-z0-9]+\.[A-Za-z0-9\.]+\.$', word):
        word_shape = 'abbreviation'
    elif re.match('[A-Za-z0-9]+\-[A-Za-z0-9\-]+.*$', word):
        word_shape = 'contains-hyphen'

    return word_shape


def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    word_lemma = sent[i][2]

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word.length': len(word),
        'word.lemma()': word_lemma,
        'word[-3:]': word.lower()[-3:],
        'word[-2:]': word.lower()[-2:],
        'word[:3]': word.lower()[:3],
        'word[:2]': word.lower()[:2],
        'word.get_shape()': get_shape(word),
        'word.get_dandhyp()': get_dandhyp(word),
        'word.get_dandsls()': get_dandsls(word),
        'word.get_type()': get_type(word),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i - 1][0]
        postag1 = sent[i - 1][1]
        word_lemma1 = sent[i - 1][2]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.length': len(word1),
            '-1:word.lemma()': word_lemma1,
            '-1:word.get_shape()': get_shape(word1),
            '-1:word.get_dandhyp()': get_dandhyp(word1),
            '-1:word.get_dandsls()': get_dandsls(word1),
            '-1:word.get_type()': get_type(word1),
            '-1:word[-2:]': word1.lower()[-2:],
            '-1:word[-3:]': word1.lower()[-3:],
            '-1:word[:2]': word1.lower()[:2],
            '-1:word[:3]': word1.lower()[:3],
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1][0]
        postag1 = sent[i + 1][1]
        word_lemma1 = sent[i + 1][2]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.length': len(word1),
            '+1:word.lemma()': word_lemma1,
            '+1:word.get_shape()': get_shape(word1),
            '+1:word.get_type()': get_type(word1),
            '+1:word.get_dandhyp()': get_dandhyp(word1),
            '+1:word.get_dandsls()': get_dandsls(word1),
            '+1:word[:2]': word1.lower()[:2],
            '+1:word[:3]': word1.lower()[:3],
            '+1:word[-2:]': word1.lower()[-2:],
            '+1:word[-3:]': word1.lower()[-3:],
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    if i > 1:
        word1 = sent[i - 2][0]
        postag1 = sent[i - 2][1]
        word_lemma1 = sent[i - 2][2]
        features.update({
            '-2:word.lower()': word1.lower(),
            '-2:word.length': len(word1),
            '-2:word.lemma()': word_lemma1,
            '-2:word.get_shape()': get_shape(word1),
            '-2:word.get_type()': get_type(word1),
            '-2:word.get_dandhyp()': get_dandhyp(word1),
            '-2:word.get_dandsls()': get_dandsls(word1),
            '-2:word[-2:]': word1.lower()[-2:],
            '-2:word[-3:]': word1.lower()[-3:],
            '-2:word[:2]': word1.lower()[:2],
            '-2:word[:3]': word1.lower()[:3],
            '-2:postag': postag1,
            '-2:postag[:2]': postag1[:2],
        })

    if i < len(sent) - 2:
        word1 = sent[i + 2][0]
        postag1 = sent[i + 2][1]
        word_lemma1 = sent[i + 2][2]
        features.update({
            '+2:word.lower()': word1.lower(),
            '+2:word.length': len(word1),
            '+2:word.lemma()': word_lemma1,
            '+2:word.get_shape()': get_shape(word1),
            '+2:word.get_type()': get_type(word1),
            '+2:word.get_dandhyp()': get_dandhyp(word1),
            '+2:word.get_dandsls()': get_dandsls(word1),
            '+2:word[:2]': word1.lower()[:2],
            '+2:word[:3]': word1.lower()[:3],
            '+2:word[-2:]': word1.lower()[-2:],
            '+2:word[-3:]': word1.lower()[-3:],
            '+2:postag': postag1,
            '+2:postag[:2]': postag1[:2],
        })

    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]


def sent2labels(sent):
    return [label for token, postag, lemma, label in sent]


def sent2tokens(sent):
    return [token for token, postag, lemma, label in sent]