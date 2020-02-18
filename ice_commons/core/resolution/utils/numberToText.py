from word2number import w2n
import re
from ice_commons.utility.custom_tokenizer import tokenize_utterance
from collections import OrderedDict

def stringToNumHandlingFunc(s):
    def text2int(textnum, numwords=None):
        if numwords is None:
            numwords = OrderedDict()
        if not numwords:
            units = [
                "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)

        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)

        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

        current = result = 0
        for word in textnum.split():
            if word not in numwords:
                raise Exception("Illegal word: " + word)

            scale, increment = numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
        number = result + current
        return number

    original = s
    if (len(s) > 0):
        if (s[len(s) - 1] != '.'):
            s = s + '.'
    ot = tokenize_utterance(s)
    otl = s.lower()
    otl = tokenize_utterance(otl)

    comma_number = ''
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
               'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
               'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
               'hundred', 'thousand', 'million', 'billion', 'point', 'and']

    units_and_tens = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                      'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                      'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
                      'ninety']

    multiples = ['billion', 'hundred', 'thousand', 'million']
    list2 = []
    word = ''
    z = 1
    list1 = otl
    data = OrderedDict()
    not_decimal = 0
    comma_numbers = []
    s_index = OrderedDict()
    s_index_copy = OrderedDict()
    s_index_count = 0

    for i in range(0, len(otl)):
        s_index[i] = otl[i]
        s_index_copy[i] = ot[i]
        s_index_count += 1

    end_comma_numbers = 0
    i = 0
    output_list = []
    _and_ = 0
    count = 0

    def front_back(original_nos):

        original_nos = tokenize_utterance(original_nos)
        front = original_nos[0]
        length = len(original_nos)
        o = ''
        if (original_nos[len(original_nos) - 1] == ','):
            original_nos.pop()
        for e in original_nos:
            o += e
        return front, length, o

    def dict_to_list(k, start, length):
        s_index2 = OrderedDict()
        for c, v in list(s_index.items()):
            s_index2[c] = v
        start_index = -1
        end_index = -1
        first = 0
        for key, value in list(s_index.items()):
            if (start == value and first == 0):
                start_index = key
                first = 1
            elif (first == 0):
                del s_index2[key]
        end_index = start_index + (length - 1)
        if (start_index == -1 or end_index == -1):
            return -1, -1
        else:
            for j in range(start_index, end_index + 1):
                del s_index2[j]

            s_index.clear()
            for c, v in list(s_index2.items()):
                s_index[c] = v

            return start_index, end_index

    ot2 = []
    while (i < len(list1) and count < s_index_count):
        I = 0
        digit = 0
        flag_continue = 0
        flag_number = 0

        if (re.match("^[0-9]+\.[0-9]+$", list1[i]) is not None or re.match("^[0-9]+$",
                                                                           list1[i]) is not None or re.match(
                "\.[0-9]+$", list1[i]) is not None):
            if (list1[i + 1] in multiples):
                multiplier = float(w2n.word_to_num(list1[i + 1]))
                list2.append(list1[i] + " " + list1[i + 1])
                list2.append(multiplier * float(list1[i]))
                ot2.append(ot[i] + " " + ot[i + 1])
                flag_number = 3
            elif (list1[i + 1] in numbers):
                list2.append(list1[i])
                flag_number = 2
                I = 1

            if (list1[i + 1] == ','):
                comma_numbers = []
                k = i
                while (re.match("^[0-9]+\.[0-9]+$", list1[k]) is not None or re.match("^[0-9]+$",
                                                                                      list1[k]) is not None or list1[
                           k] == ',' or re.match("\.[0-9]+$", list1[k]) is not None):
                    comma_numbers.append(list1[k])
                    k += 1

                k = 0
                compare_temp = ""
                full_string = ""
                stop = 0
                while (k <= len(comma_numbers) - 1):

                    compare_temp += comma_numbers[k]
                    if (compare_temp in original):
                        full_string = compare_temp
                        k += 1
                    if (compare_temp not in original):
                        compare2 = compare_temp[0:len(compare_temp) - len(comma_numbers[k])]
                        if (len(compare2) != 0):
                            compare_temp = compare2 + ' '
                            stop += 1
                        else:
                            compare_temp = ''
                    if (stop > 50):
                        k += 1

                nos = ''
                original_nos = ''
                flag = 0
                length = 0
                for z in full_string:

                    if (z == ' ' or length == len(full_string) - 1):
                        if (re.match("^[0-9]+$", z) is not None):
                            nos = nos + z
                            original_nos += z

                        if ('.' in nos and len(nos) != 0):
                            front, length2, original_nos = front_back(original_nos)
                            data['text'] = original_nos
                            data['digit'] = float(nos)

                            start, end = dict_to_list(count, front, length2)
                            data['start_index'] = start
                            data['end_index'] = end
                            output_list.append(data)
                            count += 1

                        elif (len(nos) != 0):

                            front, length2, original_nos = front_back(original_nos)
                            data['text'] = original_nos
                            data['digit'] = int(nos)

                            start, end = dict_to_list(count, front, length2)
                            data['start_index'] = start
                            data['end_index'] = end
                            output_list.append(data)
                            count += 1
                        file_name = 'resolving_numbers.json'

                        nos = ''
                        comma_number = full_string
                        original_nos = ''

                        data = OrderedDict()
                    elif (z != ',' or z == '.'):
                        original_nos += z
                        nos = nos + z
                    elif (z == ','):
                        original_nos += z
                    length += 1

                full_string = ""
                flag_number = 5
            elif (re.match("^[0-9]+\.[0-9]+$", list1[i]) is not None or re.match("\.[0-9]+$", list1[i]) is not None):
                if (list1[i + 1] not in numbers):
                    list2.append(list1[i])
                    flag_number = 2

        if (re.match("^[0-9]+$", list1[i]) is not None and list1[i + 1] not in numbers and flag_number != 5):
            list2.append(list1[i])
            flag_number = 2
            I = 1
        if (list1[i] in numbers and flag_number != 5):
            if (list1[i + 1] == 'and' or list1[i + 1] in 'And'):
                if (list1[i] in numbers and list1[i + 2] in numbers and _and_ == 0 and list1[i] not in units_and_tens):
                    list2.append(list1[i])
                    ot2.append(ot[i])
                    flag_number = 1
                    _and_ += 1
                else:
                    list2.append(list1[i])
                    ot2.append(ot[i])
                    flag_number = 0
            elif (list1[i] == 'and' or list1[i] == 'And'):
                if (_and_ == 1):
                    flag_number = 1
                    list2.append(list1[i])
                    ot2.append(ot[i])
                else:
                    flag_number = 0


            elif (list1[i + 1] not in numbers):
                list2.append(list1[i])
                ot2.append(ot[i])
                if (len(list2) == 1):
                    flag_number = 4
                else:
                    flag_number = 0
            else:
                list2.append(list1[i])
                ot2.append(ot[i])
                flag_number = 1

        if (flag_number == 0):

            if (len(list2) != 0):

                s = " ".join(list2)
                ot2 = " ".join(ot2)
                data['text'] = ot2
                data['digit'] = text2int(s)
                start, end = dict_to_list(count, list2[0], len(list2))
                data['start_index'] = start
                data['end_index'] = end
                _and_ = 0
                output_list.append(data)
                if (start != end):
                    count += end - start + 1
                else:
                    count += 1

                data = OrderedDict()
                list2 = []
                ot2 = []
            elif (re.match(";|,| |/|\?|\"|\]|\[|\(|\)|\{|\}|\t|\n|\v|\f|\r", list1[i]) is not None or list1[i] == '.' or
                  list1[i] == "'"):
                nothing = 0
            else:
                start, end = dict_to_list(count, list1[i], 1)
                if (start == -1 and end == -1):
                    do_nothing = 1
                else:
                    count = start + 1

        elif (flag_number == 2):
            if (len(list2) != 0):
                if (I == 1):
                    data['text'] = list2[0]
                    data['digit'] = int(list2[0])
                    start, end = dict_to_list(count, list2[0], 1)

                    data['start_index'] = start
                    data['end_index'] = end
                    count += 1


                else:
                    data['text'] = list2[0]
                    data['digit'] = float(list2[0])
                    start, end = dict_to_list(count, list2[0], 1)
                    data['start_index'] = start
                    data['end_index'] = end
                    count += 1

                output_list.append(data)
                data = OrderedDict()
                list2 = []

        elif (flag_number == 3):
            if (len(list2) != 0):
                list3 = list2[0].split(' ')

                data['text'] = ot2[0]
                data['digit'] = list2[1]
                start, end = dict_to_list(count, list3[0], len(list3))
                count += 2
                data['start_index'] = start
                data['end_index'] = end
                output_list.append(data)
                data = OrderedDict()
                list2 = []
                ot2 = []
                i += 1
        elif (flag_number == 4):
            if (len(list2) != 0):
                data['text'] = ot2[0]
                data['digit'] = w2n.word_to_num(list2[0])
                start, end = dict_to_list(count, list2[0], 1)
                data['start_index'] = start
                data['end_index'] = end
                output_list.append(data)
                count += 1
                data = OrderedDict()
                list2 = []
                ot2 = []
        for comma in comma_number:
            if (comma == ','):
                i += 2
        comma_number = ''

        i += 1
    return output_list
