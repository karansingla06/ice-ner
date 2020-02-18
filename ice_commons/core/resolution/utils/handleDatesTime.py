import re
import json
import moment
import pprint
import datefinder
from word2number import w2n
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

from ice_commons.core.resolution.utils import propertyFile
from ice_commons.core.resolution.utils.numberToText import stringToNumHandlingFunc
from ice_commons.utility.custom_tokenizer import tokenize_utterance

class DateUtils(object):
    """ handles dates and times in user input.
        returns: json object
        example: can i book an appointment on coming friday ?
                 [{'position': [6, 8],
                  'timestamp': '2019-01-25 00:00:00+05.50',
                  'unit': 'day',
                  'words': 'coming friday'}] """
    @staticmethod
    def set_json_time_stamp(timestamp, words, keyword):
        """ creates json time stamp object. """
        json_time_stamp = {}
        date_array = []
        if type(timestamp) != list:
            json_time_stamp['timestamp'] = [timestamp.replace('T', ' ').strip()]
        else:
            json_time_stamp['timestamp'] = timestamp
        json_time_stamp['words'] = words
        json_time_stamp['unit'] = keyword
        date_array.append(json_time_stamp.copy())
        return date_array
    @staticmethod
    def check_to_consider(string, string_list):
        """ handles special cases which are not handled
            correctly by python built-in package "datefinder"
        """
        consider_time_stamp = False
        temp_string_list = list([re.sub(r'[^ a-zA-Z0-9\'\\\/\-]', '', x) for x in string_list])
        # ignore timestamps for weekday keywords
        week_days_data = list([x for x in temp_string_list if x.lower() in propertyFile.week_day_words])
        consider_week_data = True if len(week_days_data) > 0 else False
        # ignore timestamp for string with just numbers eg. 14
        consider_numeric_data = string.isdigit()
        # ignore timestamp for strings like 12th or 3rd which are not followed by month
        temp = re.findall(r'(st|nd|rd|th)', string)
        consider_spl_words = False
        if len(temp) > 0:
            month_name_data = list([x for x in temp_string_list if x.lower() in propertyFile.month_names])
            consider_spl_words = False if len(month_name_data) > 0 else True
        consider_time_stamp = consider_week_data or consider_numeric_data or consider_spl_words
        return consider_time_stamp
    @staticmethod
    def set_time_zero(string):
        """ set time to 00:00:00 in timestamp when time not required."""
        string = str(string)
        string = string.split('T')[0] + ' ' + '00:00:00'
        return string
    @staticmethod
    def change_timestamp_format(string):
        """ change time stamp yyyy-mm-ddThh:mm:ss+05.50 to yyyy-mm-dd hh:mm:ss """
        string = string.replace('T', ' ')
        string = string.split('+')[0]
        return string
    @staticmethod
    def check_past_tense_in_input(string):
        """ return 'True' if user input is in past tense."""
        res_tense = pos_tag(word_tokenize(string))
        check_past_tense = False
        for i in range(len(res_tense)):
            if ('VBD' in res_tense[i][1]) or ('VBN' in res_tense[i][1]):
                check_past_tense = True
        return check_past_tense
    @staticmethod
    def convert_list_tostring(arr_list):
        """ append list data to form sentence. """
        data = ''
        if type(arr_list) is str:
            data = arr_list
        else:
            data = ' '.join(arr_list)
        return data.strip()
    @staticmethod
    def get_words(case_sensitive_data, start, end):
        """ returns case sensitive user input data."""
        words = ''
        for k in range(start, end):
            words += case_sensitive_data[k] + ' '
        return words.strip()
    def handle_dates(self, string):
        """  uses python package 'datfinder' to
             handle dates in user input.
             example : 2nd may 2018 , 13/05/1996
        """
        string += ' '
        json_time_stamp = {}
        date_array = []
        temp_list = string.split(' ')
        try:
            
            re_data = re.compile('|'.join(propertyFile.week_day_words), re.IGNORECASE)
            re_to = re.compile(' to ', re.IGNORECASE)
            string = re_data.sub("x", string)
            string = re_to.sub(" upto ", string)
            matches = datefinder.find_dates(string, index=True)
            for match in matches:
                remove_duplicate_str = []
                for i in range(len(date_array)):
                    pos = date_array[i]['position']
                    remove_duplicate_str.append(pos[0])
                    remove_duplicate_str.append(pos[1])          
                date = match
                sub_temp_list = string[date[1][0]:date[1][1]].strip().split(' ')
                for i in range(0, len(remove_duplicate_str), 2 ):
                    start = remove_duplicate_str[i]
                    end = remove_duplicate_str[i+1]
                    for j in range(start, end):
                        temp_list[j] = ' '
                index_list = []                
                for index in range(len(sub_temp_list)):
                    if sub_temp_list[index] in propertyFile.extra_tokens:
                        index_list.append(sub_temp_list[index])                
                for i in range(len(index_list)):
                    if index_list[i] != 'at':
                        sub_temp_list.remove(index_list[i])
                    else:
                        if i == 0:
                            sub_temp_list.remove(index_list[i])
                position = list(temp_list.index(sub_temp_list[x]) for x in range(len(sub_temp_list)))
                json_time_stamp['timestamp'] = [date[0].strftime("%Y-%m-%d %H:%M:%S")]
                json_time_stamp['position'] = [position[0], position[-1] + 1]
                temp_str = ' '.join(sub_temp_list)
                temp_str = temp_str.replace('  ', ' ').strip()
                fn_not_considered = self.check_to_consider(temp_str, sub_temp_list)
                if fn_not_considered:
                    continue
                json_time_stamp['words'] = temp_str.strip()
                json_time_stamp['unit'] = 'date'
                date_array.append(json_time_stamp.copy())
            return date_array
        except:
            return []
    def handle_common_words(self, string):
        """ handles and returns timestamps for common words in user input.
            example : tomorrow, day before yesterday
        """
        res_time_stamp = []
        time_period = {
            "now": str(moment.now()).split('+')[0],
            "today": str(moment.now()).split('T')[0] + " 00:00:00",
            "tomorrow": str(moment.now().add(days=1)).split('T')[0] + " 00:00:00",
            "yesterday": str(moment.now().subtract(days=1)).split('T')[0] + " 00:00:00",
            "day after tomorrow": str(moment.now().add(days=2)).split('T')[0] + " 00:00:00",
            "day before yesterday": str(moment.now().subtract(days=2)).split('T')[0] + " 00:00:00",
            "tonite": str(moment.now()).split('T')[0] + " 20:00:00",
            "tomorrow morning": str(moment.now().add(days=1)).split('T')[0] + " 06:00:00",
            "tomorrow afternoon": str(moment.now().add(days=1)).split('T')[0] + " 12:00:00",
            "tomorrow night": str(moment.now().add(days=1)).split('T')[0] + " 20:00:00",
            "tomorrow evening": str(moment.now().add(days=1)).split('T')[0] + " 16:00:00",
            "yesterday morning": str(moment.now().subtract(days=1)).split('T')[0] + " 06:00:00",
            "yesterday afternoon": str(moment.now().subtract(days=1)).split('T')[0] + " 12:00:00",
            "yesterday night": str(moment.now().subtract(days=1)).split('T')[0] + " 20:00:00",
            "yesterday evening": str(moment.now().subtract(days=1)).split('T')[0] + " 16:00:00",
            "today morning": str(moment.now()).split('T')[0] + " 06:00:00",
            "today afternoon": str(moment.now()).split('T')[0] + " 12:00:00",
            "today night": str(moment.now()).split('T')[0] + " 20:00:00",
            "today evening": str(moment.now()).split('T')[0] + " 16:00:00",
            "morning": str(moment.now()).split('T')[0] + " 06:00:00",
            "afternoon": str(moment.now()).split('T')[0] + " 12:00:00",
            "night": str(moment.now()).split('T')[0] + " 20:00:00",
            "evening": str(moment.now()).split('T')[0] + " 16:00:00"
        }
        date = time_period[string]
        res_time_stamp = self.set_json_time_stamp(date, string, 'day')
        return res_time_stamp
    def handle_festival_names(self, string, check_past_tense):
        """ handles and returns timestamps for festival names in user input."""
        res_time_stamp = []
        fest_data = list([x for x in propertyFile.festival_names if x.lower() in string.lower()])
        if len(fest_data) > 0 and fest_data is not None:
            next_data = list([x for x in propertyFile.next_words if x.lower() in string.lower()])
            prev_data = list([x for x in propertyFile.previous_words if x.lower() in string.lower()])
            day_num = moment.now().day
            month = moment.now().month
            year = moment.now().year
            if 'christmas' in fest_data[0]:
                if len(next_data) > 0:
                    if (month == 12 and day_num > 25):
                        year_num = year + 1
                    else:
                        year_num = year
                elif len(prev_data) > 0 or check_past_tense:
                    if (month == 12 and day_num > 25):
                        year_num = year
                    else:
                        year_num = year - 1
                else:
                    year_num = year
                day = str(moment.date(year_num, 12, 25, 0, 0, 0))
                day = day.split('+')[0]
            elif 'thanksgiving' in fest_data[0]:
                if len(next_data) > 0:
                    if ((month == 11 and day_num > 22) or month == 12):
                        year_num = year + 1
                    else:
                        year_num = year
                elif len(prev_data) > 0 or check_past_tense:
                    if ((month == 11 and day_num > 22) or month == 12):
                        year_num = year
                    else:
                        year_num = year - 1
                else:
                    year_num = year
                day = str(moment.date(year_num, 11, 22, 0, 0, 0))
                day = day.split('+')[0]
            elif 'new year' in fest_data[0]:
                if len(next_data) > 0:
                    year_num = year + 1
                elif len(prev_data) > 0 or check_past_tense:
                    if (month == 1 and day_num == 1):
                        year_num = year - 1
                    else:
                        year_num = year
                else:
                    year_num = year + 1
                day = str(moment.date(year_num, 1, 1, 0, 0, 0))
                day = day.split('+')[0]
            res_time_stamp = self.set_json_time_stamp(day, string, 'festival')
        return res_time_stamp
    def handle_weekdays(self, string, check_past_tense):
        """ handles and returns timestamps for weekdays in user input."""
        res_time_stamp = []
        week_day_data = list([x for x in propertyFile.week_day_words if x.lower() in string.lower()])
        week_day_dict = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4,
                       "friday": 5, "saturday": 6, "sunday": 7}
        if (len(week_day_data) > 0 and week_day_data is not None):
            next_data = list([x for x in propertyFile.next_words if x.lower() in string.lower()])
            prev_data = list([x for x in propertyFile.previous_words if x.lower() in string.lower()])
            current_day = moment.now().weekday
            week_day = week_day_dict.get(week_day_data[0])
            no_days = current_day - week_day
            if len(prev_data) > 0 or check_past_tense:
                if no_days <= 0:
                    no_days = 7 + no_days
                day = str(moment.now().subtract(days=no_days))
            else:
                if no_days == 0:
                    no_days += 7
                elif week_day < current_day:
                    no_days = 7 - no_days
                else:
                    no_days = no_days * -1
                day = str(moment.now().add(days=no_days))
            day = self.set_time_zero(day)
            day = day.split('+')[0]
            res_time_stamp = self.set_json_time_stamp(day, string, 'day')
        return res_time_stamp
    def handle_time_period(self, string, check_past_tense, no_days):
        """ handle and return timestamp for keywords (weeks, months, hours etc ) in user input."""
        res_time_stamp = []
        temp_list = string.split(' ')
        time_period_data = list([x for x in propertyFile.time_period_words if x.lower() in string.lower()])
        if len(time_period_data) > 0 and time_period_data is not None:
            temp_data_list = propertyFile.time_period_words
            for i in range(0, len(temp_data_list), 2):
                if temp_data_list[i] in time_period_data and temp_data_list[i + 1] in temp_list:
                    time_period_data.remove(temp_data_list[i])
            next_data = list([x for x in propertyFile.next_words if x.lower() in string.lower()])
            prev_data = list([x for x in propertyFile.previous_words if x.lower() in string.lower()])
            current_data = list([x for x in propertyFile.current_words if x.lower() in string.lower()])
            if len(current_data) > 0:
                for i in range(0, len(temp_data_list), 2):
                    if temp_data_list[i] in time_period_data or temp_data_list[i + 1] in time_period_data:
                        day = str(moment.now())
                        day = self.change_timestamp_format(day)
                        unit = temp_data_list[i]
                        if temp_data_list[i] != 'hour' and temp_data_list[i] != 'minute':
                            day = self.set_time_zero(day.split(' ')[0])
            elif len(next_data) > 0:
                for i in range(0, len(temp_data_list), 2):
                    if temp_data_list[i] in time_period_data or temp_data_list[i + 1] in time_period_data:
                        key_data = temp_data_list[i + 1]
                        unit = temp_data_list[i]
                        if 'next' in next_data or 'coming' in next_data or 'future' in next_data:
                            temp_arr = []
                            for j in range(1, no_days + 1):
                                if temp_data_list[i] != 'hour' and temp_data_list[i] != 'minute':
                                    temp = self.set_time_zero(str(moment.now().add(key_data, j)))
                                    temp_arr.append(temp)
                                else:
                                    temp = str(moment.now().add(key_data, j))
                                    temp = temp.replace('T', ' ')
                                    temp_arr.append(temp)
                            day = temp_arr
                        else:
                            day = str(moment.now().add(key_data, no_days))
                            day = self.change_timestamp_format(day)
                            unit = temp_data_list[i]
                            if temp_data_list[i] != 'hour' and temp_data_list[i] != 'minute':
                                day = self.set_time_zero(day.split(' ')[0])
            elif len(prev_data) > 0:
                for i in range(0, len(temp_data_list), 2):
                    if temp_data_list[i] in time_period_data or temp_data_list[i + 1] in time_period_data:
                        key_data = temp_data_list[i + 1]
                        unit = temp_data_list[i]
                        if 'last' in prev_data or 'previous' in prev_data or 'past' in prev_data:
                            temp_arr = []
                            for j in range(1, no_days + 1):
                                if 'hour' not in temp_data_list[i] and 'minute' not in temp_data_list[i]:
                                    temp = self.set_time_zero(str(moment.now().subtract(key_data, j)))
                                    temp_arr.append(temp)
                                else:
                                    temp = str(moment.now().subtract(key_data, j))
                                    temp = temp.replace('T', ' ')
                                    temp_arr.append(temp)
                            day = temp_arr
                        else:
                            day = str(moment.now().subtract(key_data, no_days))
                            day = self.change_timestamp_format(day)
                            unit = temp_data_list[i]
                            if temp_data_list[i] != 'hour' and temp_data_list[i] != 'minute':
                                day = self.set_time_zero(day.split(' ')[0])
            elif check_past_tense:
                for i in range(0, len(temp_data_list), 2):
                    if temp_data_list[i] in time_period_data or temp_data_list[i + 1] in time_period_data:
                        key_data = temp_data_list[i + 1]
                        day = str(moment.now().subtract(key_data, no_days))
                        day = self.change_timestamp_format(day)
                        unit = temp_data_list[i]
                        if temp_data_list[i] != 'hour' and temp_data_list[i] != 'minute':
                            day = self.set_time_zero(day.split(' ')[0])
            else:
                for i in range(0, len(temp_data_list), 2):
                    if temp_data_list[i] in time_period_data or temp_data_list[i + 1] in time_period_data:
                        key_data = temp_data_list[i + 1]
                        day = str(moment.now().add(key_data, no_days))
                        day = self.change_timestamp_format(day)
                        unit = temp_data_list[i]
                        if temp_data_list[i] != 'hour' and temp_data_list[i] != 'minute':
                            day = self.set_time_zero(day.split(' ')[0])
            res_time_stamp = self.set_json_time_stamp(day, string, unit)
        return res_time_stamp
    def parse_date(self, user_input):
        """ handles user input, checks for main keywords and passes these keywords as
            parameters to specific functions. """
        tokens_correct = tokenize_utterance(user_input)
        user_input = " ".join(tokens_correct)
        actual_data = user_input
        user_input = user_input.lower()
        case_sensitive_input = actual_data.split(' ')
        word_list = user_input.split(' ')
        del_pos = []
        data_content = []
        supporting_data_content = []
        result_data = []
        # identify main keywords in user data and store it in 'data_content' array with it's index value.
        # 'data_content' format - eg. ['day after tomorrow', [], main_data2, [start_index2, end_index2], ... ]
        main_words = propertyFile.main_words
        for i in range(len(word_list)):
            words = word_list[i]
            try:
                # handle main keywords with multiple words (day after tomorrow, new year, etc)
                if word_list[i] == 'day':
                    try:
                        check_data = False
                        if (word_list[i+1] == 'after' and word_list[i+2] == 'tomorrow') or (word_list[i+1] == 'before' and word_list[i+2] == 'yesterday'):
                            position = [i, i+3]
                            check_data = True
                        else:
                            main_words.index(word_list[i])
                            position = [i, i+1]
                    except:
                        main_words.index(word_list[i])
                        position = [i, i+1]
                    if check_data:
                        words = word_list[i] + ' ' + word_list[i+1] + ' ' + word_list[i+2]
                        del_pos.append(i+1)
                        del_pos.append(i+2)
                elif word_list[i] == 'tomorrow' or word_list[i] == 'today' or word_list[i] == 'yesterday':
                    try:
                        check_data = False
                        if (word_list[i+1] == 'morning') or (word_list[i+1] == 'night') or (word_list[i+1] == 'afternoon') or (word_list[i+1] == 'evening'):
                            position = [i, i+2]
                            check_data = True
                        else:
                            main_words.index(word_list[i])
                            position = [i, i+1]
                    except:
                        main_words.index(word_list[i])
                        position = [i, i+1]
                    if check_data:
                        words = word_list[i] + ' ' + word_list[i+1]
                        del_pos.append(i+1)
                elif word_list[i] == 'new':
                    try:
                        check_data = False
                        if word_list[i+1] == 'year':
                            position = [i, i+2]
                            check_data = True
                        else:
                            main_words.index(word_list[i])
                            position = [i, i+1]
                    except:
                        main_words.index(word_list[i])
                        position = [i, i+1]
                    if check_data:
                        words = word_list[i] + ' ' + word_list[i+1]
                        del_pos.append(i+1)
                elif word_list[i] == 'now':
                    try:
                        if (word_list[i-1] == 'from'):
                            position = []
                        else:
                            words.index(word_list[i])
                            position = [i, i+1]
                    except:
                        main_words.index(word_list[i])
                        position = [i, i+1]
                else:
                    main_words.index(word_list[i])
                    position = [i, i+1]
            except:
                position = []
            if len(position) > 0 and position[0] not in del_pos:
                data_content.append(words)
                data_content.append(position)
        # identify supporting keywords in user data and store it in 'supporting_data_content' array with it's index value.
        # 'supporting_data_content' format - [supp_data1, [start_index1, end_index1], supp_data2, [start_index2, end_index2], ... ]
        for i in range(len(word_list)):
            word = word_list[i]
            check_data = False
            try:
                # handle supporting keywords with multiple words (eg. from now)
                if word_list[i] == 'from':
                    try:
                        if word_list[i+1] == 'now':
                            position = [i, i+1]
                            check_data = True
                        else:
                            position = []
                    except:
                        propertyFile.supporting_words.index(word_list[i])
                        position = [i, i+1]
                    if check_data:
                        word = word_list[i] + ' ' + word_list[i+1]
                        del_pos.append(i+1)
                else:
                    propertyFile.supporting_words.index(word_list[i])
                    position = [i, i+1]
            except:
                position = []
            if len(position) > 0 and position[0] not in del_pos:
                supporting_data_content.append(word)
                supporting_data_content.append(position)
        # recognize numbers (even words eg. forty five) in user input and store in array 'days'.
        try:
            days = stringToNumHandlingFunc(user_input)
        except:
            days = []
        # check if user input is in past tense
        check_past_tense = self.check_past_tense_in_input(user_input)
        # handle all the identified main keywords
        for i in range(0, len(data_content), 2):
            if data_content[i] in propertyFile.common_words:
                timestamp_data_common_words = self.handle_common_words(data_content[i])
                timestamp_data_common_words[0]['position'] = data_content[i + 1]
                timestamp_data_common_words[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                     data_content[i + 1][-1])
                result_data.append(timestamp_data_common_words[0])
            elif data_content[i] in propertyFile.festival_names:
                least_diff = []
                check_diff = False
                check_diff_sec = True
                if len(supporting_data_content) > 0:
                    for j in range(0, len(supporting_data_content), 2):
                        pos = data_content[i + 1][0]
                        if ((supporting_data_content[j] in propertyFile.selected_supporting_words) and (
                                supporting_data_content[j + 1][0] < pos)):
                            diff = data_content[i + 1][0] - supporting_data_content[j + 1][0]
                            if diff < 5:
                                if diff == 1:
                                    check_diff = False
                                else:
                                    check_diff = True
                                if len(least_diff) == 0:
                                    least_diff.append(supporting_data_content[j])
                                    least_diff.append(supporting_data_content[j + 1])
                                else:
                                    if (least_diff[1][0] < supporting_data_content[j + 1][0]):
                                        least_diff = []
                                        least_diff.append(supporting_data_content[j])
                                        least_diff.append(supporting_data_content[j + 1])
                                        check_diff_sec = False
                    if len(least_diff) > 0:
                        timestamp_data_fun = self.handle_festival_names(least_diff[0] + ' ' + data_content[i], check_past_tense)
                        if check_diff and check_diff_sec:
                            timestamp_data_fun[0]['position'] = data_content[i + 1]
                            timestamp_data_fun[0]['words'] = self.convert_list_tostring(
                                case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][-1]])
                        else:
                            timestamp_data_fun[0]['position'] = [least_diff[1][0], data_content[i + 1][1]]
                            timestamp_data_fun[0]['words'] = self.convert_list_tostring(
                                case_sensitive_input[least_diff[1][0]:least_diff[1][1]])
                            timestamp_data_fun[0]['words'] += ' ' + self.convert_list_tostring(
                                case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][-1]])
                    else:
                        timestamp_data_fun = self.handle_festival_names(data_content[i], check_past_tense)
                        timestamp_data_fun[0]['position'] = data_content[i + 1]
                        timestamp_data_fun[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                     data_content[i + 1][1])
                else:
                    timestamp_data_fun = self.handle_festival_names(data_content[i], check_past_tense)
                    timestamp_data_fun[0]['position'] = data_content[i + 1]
                    timestamp_data_fun[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                 data_content[i + 1][1])
                result_data.append(timestamp_data_fun[0])
            elif data_content[i] in propertyFile.week_day_words:
                least_diff = []
                check_diff = False
                check_diff_sec = True
                if len(supporting_data_content) > 0:
                    for j in range(0, len(supporting_data_content), 2):
                        pos = data_content[i + 1][0]
                        if ((supporting_data_content[j] in propertyFile.selected_supporting_words) and (
                                supporting_data_content[j + 1][0] < pos)):
                            diff = data_content[i + 1][0] - supporting_data_content[j + 1][0]
                            if diff < 5:
                                if diff == 1:
                                    check_diff = False
                                else:
                                    check_diff = True
                                if len(least_diff) == 0:
                                    least_diff.append(supporting_data_content[j])
                                    least_diff.append(supporting_data_content[j + 1])
                                else:
                                    if (least_diff[1][0] < supporting_data_content[j + 1][0]):
                                        least_diff = []
                                        least_diff.append(supporting_data_content[j])
                                        least_diff.append(supporting_data_content[j + 1])
                                        check_diff_sec = False
                    if len(least_diff) > 0:
                        timestamp_data_week = self.handle_weekdays(least_diff[0] + ' ' + data_content[i], check_past_tense)
                        if check_diff and check_diff_sec:
                            timestamp_data_week[0]['position'] = data_content[i + 1]
                            timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                        else:
                            timestamp_data_week[0]['position'] = [least_diff[1][0], data_content[i + 1][1]]
                            timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                case_sensitive_input[least_diff[1][0]:least_diff[1][1]])
                            timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                    else:
                        timestamp_data_week = self.handle_weekdays(data_content[i], check_past_tense)
                        timestamp_data_week[0]['position'] = data_content[i + 1]
                        timestamp_data_week[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                      data_content[i + 1][1])
                else:
                    timestamp_data_week = self.handle_weekdays(data_content[i], check_past_tense)
                    timestamp_data_week[0]['position'] = data_content[i + 1]
                    timestamp_data_week[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                  data_content[i + 1][1])
                result_data.append(timestamp_data_week[0])
            elif data_content[i] in propertyFile.time_period_words:
                least_diff = []
                valid_num = []
                check_diff = False
                check_diff_sec = True
                if len(days) > 0:
                    no_days_arr = []
                    for j in range(len(days)):
                        arr = list(days[j].values())
                        no_days_arr.extend(arr)
                    for k in range(0, len(no_days_arr), 4):
                        if no_days_arr[k + 3] + 1 == data_content[i + 1][0]:
                            no_day = no_days_arr[k + 1]
                            valid_num.append(no_days_arr[k])
                            valid_num.append(no_days_arr[k + 1])
                            valid_num.append(no_days_arr[k + 2])
                            valid_num.append(no_days_arr[k + 3])
                    if len(valid_num) == 0:
                        no_day = 1
                else:
                    no_day = 1
                if len(supporting_data_content) > 0:
                    for j in range(0, len(supporting_data_content), 2):
                        pos = data_content[i + 1][0]
                        pos_supp = supporting_data_content[j + 1][0]
                        # checking for first set of supporting data (eg. next, previous, last).
                        # these supporting data occur before main data. eg. next year
                        if ((supporting_data_content[j] in propertyFile.first_part_supporting_words) and (pos_supp < pos)):
                            diff = pos - pos_supp
                            if diff <= 5:
                                if (diff > 1 and len(valid_num) == 0) or (diff > 2 and len(valid_num) != 0):
                                    check_diff = True
                                if len(least_diff) == 0:
                                    least_diff.append(supporting_data_content[j])
                                    least_diff.append(supporting_data_content[j + 1])
                                else:
                                    if (least_diff[1][0] < pos_supp):
                                        least_diff = []
                                        least_diff.append(supporting_data_content[j])
                                        least_diff.append(supporting_data_content[j + 1])
                                        check_diff_sec = False
                        # checking for second set of supporting data (eg. ago, from now ) and set check_second_supp as True
                        # these supporting data occur after main data. eg. year ago
                        elif ((supporting_data_content[j] in propertyFile.second_part_supporting_words) and (pos_supp > pos)):
                            diff = pos_supp - pos
                            if diff <= 5:
                                if (diff > 1 and len(valid_num) == 0) or (diff > 2 and len(valid_num) != 0):
                                    check_diff = True
                                if len(least_diff) == 0:
                                    least_diff.append(supporting_data_content[j])
                                    least_diff.append(supporting_data_content[j + 1])
                                else:
                                    if (least_diff[1][0] < pos_supp):
                                        least_diff = []
                                        least_diff.append(supporting_data_content[j])
                                        least_diff.append(supporting_data_content[j + 1])
                    if len(least_diff) > 0:
                        least_pos_supp = least_diff[1][0]
                        if (least_diff[0] in propertyFile.first_part_supporting_words):
                            if check_diff and check_diff_sec:
                                if len(valid_num) > 0:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    if valid_num[2] == valid_num[3]:
                                        timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                            case_sensitive_input[valid_num[2]])
                                    else:
                                        timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                            case_sensitive_input[valid_num[2]:valid_num[3] + 1])
                                    timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                        case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                    timestamp_data_week[0]['position'] = [valid_num[2], data_content[i + 1][1]]
                                else:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                        case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                    timestamp_data_week[0]['position'] = data_content[i + 1]
                            else:
                                if len(valid_num) > 0:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                        case_sensitive_input[least_pos_supp])
                                    if valid_num[2] == valid_num[3]:
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[valid_num[2]])
                                    else:
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[valid_num[2]:valid_num[3] + 1])
                                    timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                        case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                    timestamp_data_week[0]['position'] = [least_pos_supp, data_content[i + 1][1]]
                                else:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                        case_sensitive_input[least_pos_supp])
                                    timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                        case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                    timestamp_data_week[0]['position'] = [least_pos_supp, data_content[i + 1][1]]
                        else:
                            if check_diff and check_diff_sec:
                                if len(valid_num) > 0:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    timestamp_data_week[0]['position'] = [valid_num[2], data_content[i + 1][1]]
                                    if valid_num[2] == valid_num[3]:
                                        timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                            case_sensitive_input[valid_num[2]])
                                    else:
                                        timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                            case_sensitive_input[valid_num[2]:valid_num[3] + 1])
                                    timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                        case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                else:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    timestamp_data_week[0]['position'] = data_content[i + 1]
                                    timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                        case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                            else:
                                if len(valid_num) > 0:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    if len(least_diff[0].split(' ')) > 1:
                                        timestamp_data_week[0]['position'] = [valid_num[2], least_pos_supp + 2]
                                        if valid_num[2] == valid_num[3]:
                                            timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                                case_sensitive_input[valid_num[2]])
                                        else:
                                            timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                                case_sensitive_input[valid_num[2]:valid_num[3] + 1])
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[least_diff[1][0]:least_diff[1][1] + 1])
                                    else:
                                        timestamp_data_week[0]['position'] = [valid_num[2], least_pos_supp + 1]
                                        if valid_num[2] == valid_num[3]:
                                            timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                                case_sensitive_input[valid_num[2]])
                                        else:
                                            timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                                case_sensitive_input[valid_num[2]:valid_num[3] + 1])
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[least_pos_supp])
                                else:
                                    timestamp_data_week = self.handle_time_period(least_diff[0] + ' ' + data_content[i],
                                                                              check_past_tense, no_day)
                                    if len(least_diff[0].split(' ')) > 1:
                                        timestamp_data_week[0]['position'] = [data_content[i + 1][0], least_pos_supp + 2]
                                        timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                            case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[least_diff[1][0]:least_diff[1][1]])
                                    else:
                                        timestamp_data_week[0]['position'] = [data_content[i + 1][0], least_pos_supp + 1]
                                        timestamp_data_week[0]['words'] = self.convert_list_tostring(
                                            case_sensitive_input[data_content[i + 1][0]:data_content[i + 1][1]])
                                        timestamp_data_week[0]['words'] += ' ' + self.convert_list_tostring(
                                            case_sensitive_input[least_diff[1][0]:least_diff[1][1]])
                    else:
                        if len(valid_num) > 0:
                            timestamp_data_week = self.handle_time_period(data_content[i], check_past_tense, no_day)
                            timestamp_data_week[0]['position'] = [valid_num[2], data_content[i + 1][1]]
                            timestamp_data_week[0]['words'] = self.get_words(case_sensitive_input, valid_num[2],
                                                                          data_content[i + 1][1])
                        else:
                            timestamp_data_week = self.handle_time_period(data_content[i], check_past_tense, no_day)
                            timestamp_data_week[0]['position'] = data_content[i + 1]
                            timestamp_data_week[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                          data_content[i + 1][1])
                        timestamp_data_week[0]['timestamp'] = ''
                    result_data.append(timestamp_data_week[0])
                else:
                    if len(valid_num) > 0:
                        timestamp_data_week = self.handle_time_period(data_content[i], check_past_tense, no_day)
                        timestamp_data_week[0]['words'] = self.get_words(case_sensitive_input, valid_num[2],
                                                                      data_content[i + 1][1])
                        timestamp_data_week[0]['position'] = [valid_num[2], data_content[i + 1][1]]
                    else:
                        timestamp_data_week = self.handle_time_period(data_content[i], check_past_tense, no_day)
                        timestamp_data_week[0]['words'] = self.get_words(case_sensitive_input, data_content[i + 1][0],
                                                                      data_content[i + 1][1])
                        timestamp_data_week[0]['position'] = data_content[i + 1]
                    timestamp_data_week[0]['timestamp'] = ''
                    result_data.append(timestamp_data_week[0])
        # python package 'datefinder' in function 'handle_dates' checks for date and returns timestamp
        timestamp_data_date = self.handle_dates(actual_data)
        if len(timestamp_data_date) > 0:
            for i in range(len(timestamp_data_date)):
                result_data.append(timestamp_data_date[i])
        return result_data
