import configparser
import os

config = configparser.RawConfigParser()
user_dir = os.path.expanduser('~')
configFilePath = os.path.join(user_dir,'variation_settings.conf')

if not os.path.exists(configFilePath):
    raise Exception("variation_settings.conf file not exists in {}".format(user_dir))
config.read(configFilePath)

cparser_flag = int(config.get('CONFIG', 'cparser_flag'))


