
import os
import sys


sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))

from ice_commons.utility.cipher import encrypt
from pydash import get
from ice_commons.data.dl.manager import DatasourceManager




def encrypt_missed_utterance():
    '''
    uncache model if their last date of access more than 60 days.
    '''
    try:
        manager = DatasourceManager()
        query = {}
        data = manager.find_all_model(query)
        for document in data:
            try:
                missed_utterances= get(document,'missedUtterances',[])
                serviceid= document['serviceid']
                encrypted = []
                if len(missed_utterances) != 0:
                    for item in missed_utterances:
                        encrypted.append(encrypt(item))
                    manager.encrypt_missed_utterances(serviceid,encrypted)
                    print('successfully updated')
                else:
                    print('no missed_utterances, empty list')

            except Exception as e:
                print("exception : ",e)
    except Exception as e:
        print("exception : ",e)



if __name__=="__main__":
    print('----------------------starting -------------------------- ')
    encrypt_missed_utterance()