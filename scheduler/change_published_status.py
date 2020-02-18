
import os
import sys


sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))

from pydash import get
from ice_commons.data.dl.manager import ProjectManager




def change_publish_status():
    '''
    uncache model if their last date of access more than 60 days.
    '''
    try:
        manager = ProjectManager()
        query = {}
        data = manager.find_all_model(query)
        for document in data:
            try:
                ner_status= get(document,'ner.status',"new")
                ir_status= get(document,'ir.status',"new")
                print(ner_status, ir_status)
                serviceid= document['serviceid']

                if ner_status=="published" and ir_status=="published":
                    ner_status='trained'
                    ir_status = 'trained'
                    print('condition1')

                elif ner_status=="published" and ir_status!="published":
                    ner_status = 'trained'
                    print('condition2')

                elif ir_status=="published" and ner_status!="published":
                    ir_status = 'trained'
                    print('condition3')

                manager.update_ir_ner_status(serviceid, ner_status, ir_status)

            except Exception as e:
                print("exception : ",e)
    except Exception as e:
        print("exception : ",e)



if __name__=="__main__":
    print('----------------------starting -------------------------- ')
    change_publish_status()
