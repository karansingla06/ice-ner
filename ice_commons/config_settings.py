from configparser import SafeConfigParser
import os

app_config = {}


# class FakeSection(object):
#     def __init__(self, fp):
#         self.fp = fp
#         self.section_head = '[verbis]\n'
#
#     def readline(self):
#         if self.section_head:
#             self.section_head = None
#             return '[verbis]\n'
#         else:
#             return self.fp.readline()


def parse_config_file():
    config = SafeConfigParser()
    user_dir = os.path.expanduser('~')
    config_file = os.path.join(user_dir, '.verbis', 'settings.conf')
    if not os.path.exists(config_file):
        raise Exception("settings.conf file not exists in {}".format(os.path.join(user_dir, '.verbis')))
    with open(config_file, 'r') as fp:
        file_content = '[verbis]\n' + fp.read()
        config.read_string(file_content)
    return config.items('verbis')


property_list = parse_config_file()
for property_each in property_list:
    var_name = property_each[0].upper()
    if var_name in list(os.environ.keys()) and os.environ[var_name] and os.environ[var_name] != "":
        app_config[var_name] = os.environ[var_name]
    else:
        app_config[var_name] = property_each[1]

