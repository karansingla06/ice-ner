# from __future__ import unicode_literals
import re

title_list = ["mr", "mrs", "ms", "miss", "hon", "mx", "fr", "dr", "br", "sr", "rt", "prof", "doc", "pr", "rev", "pres",
              "gov", "ofc", "vc"]


def tokenize_utterance(input_string):
    split_array = (re.split('(;|,| |/|\?|\"|\]|\[|\(|\)|\{|\}|\t|\n|\v|\f|\r)', input_string))
    tokens = []
    for word_each in split_array:
        if not word_each.isspace() and word_each != "":
            if re.search('\.+$', word_each):
                length = len(word_each)
                index = 1
                ending_dot_array = []
                if word_each[:length - index].lower() not in title_list:
                    while index < length and word_each[length - index] == '.':
                        ending_dot_array.append('.')
                        index += 1
                ending_dot_array.append(word_each[0:length - (index - 1)])
                ending_dot_array = list(reversed(ending_dot_array))
                tokens.extend(ending_dot_array)
            else:
                tokens.append(word_each)
    return tokens
