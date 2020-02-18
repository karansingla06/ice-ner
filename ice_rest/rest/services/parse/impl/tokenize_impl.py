from ice_commons.utility.custom_tokenizer import tokenize_utterance as custom_tokenize_utterance

def tokenize_utterance(input_string):
    tokens = custom_tokenize_utterance(input_string)
    response = {
        "tokens": tokens
    }
    return response
