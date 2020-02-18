""" list of user input key words handled in "dateUtils" program. """
# main keywords to be searched in user input
main_words = ["year", "years", "month", "months", "week", "weeks", "days", "day", "hours",
             "hour", "minutes", "minute", "today", "tomorrow", "yesterday",
             "day after tomorrow", "day before yesterday", "morning", "afternoon", "night",
             "evening", "tonite", "now", "monday", "tuesday", "wednesday", "thursday",
             "friday", "saturday", "sunday", "christmas", "new year", "thanksgiving","tomorrow morning", 
             "tomorrow afternoon", "tomorrow night", "tomorrow evening", "yesterday morning",
             "yesterday afternoon", "yesterday night", "yesterday evening", "today morning",
             "today afternoon", "today night", "today evening" ]
# supporting words to be serached in user input [supports "main keywords"]
supporting_words = ["next", "coming", "later", "after", "current", "this",
                   "last", "previous", "ago", "past", "before", "from now",
                   "future"]
# main keywords handled by function "common_words_fun"
common_words = ["today", "tomorrow", "yesterday", "day after tomorrow",
               "day before yesterday", "morning", "afternoon", "night", "evening",
               "now", "tonite", "tomorrow morning", "tomorrow afternoon", "tomorrow night", 
               "tomorrow evening", "yesterday morning", "yesterday afternoon", "yesterday night",
                "yesterday evening", "today morning", "today afternoon", "today night", "today evening" ]
# main keywords handled by function "fest_words_fun"
festival_names = ["christmas", "new year", "thanksgiving"]
# main keywords handled by function "time_period_fun"
time_period_words = ["year", "years", "month", "months", "week", "weeks", "day",
                   "days", "hour", "hours", "minute", "minutes"]
# supporting words handled by function "time_period_fun"
first_part_supporting_words = ["next", "coming", "after", "current", "this", "last",
                            "previous", "past", "before"]
# supporting words handled by function "time_period_fun"
second_part_supporting_words = ["ago", "later", "from now", "before"]
# main keywords handled by function "week_days_fun"
week_day_words = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
                "sunday"]
# supporting words handled by function "fest_words_fun" and "week_days_fun"
selected_supporting_words = ["next", "coming", "this", "last", "previous", "past"]
# extra tokens to be removed from python package datefinder's result.
extra_tokens = ["due", "by", "on", "during", "standard", "daylight", "savings", "time",
                "dated", "date", "of", "to", "through", "between", "until", "at", "day", "next", "last"]
# keywords referring future
next_words = ["next", "coming", "later", "future", "after", "from now"]
# keywords referring past
previous_words = ["last", "previous", "ago", "past", "before"]
# keywords referring to present
current_words = ["current", "this"]
# keywords representing months
month_names = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
              "november", "december", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "sept", "oct",
              "nov", "dec"]

