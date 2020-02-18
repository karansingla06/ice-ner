import os
from fnmatch import fnmatch
import ast
from collections import namedtuple

import_details = namedtuple("Import", ["module", "name", "alias"])


def get_commons_imports(path):
    with open(path) as fh:
       root = ast.parse(fh.read(), path)

    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            continue
        for n in node.names:
            yield import_details(module, n.name.split('.'), n.asname)




commons_file_type = "*.py"
#for path, subdirs, files in os.walk('./ice_commons/'):
 #   for name in files:
  #      file_path= os.path.join(path, name)
   #     if fnmatch(name, commons_file_type):
    #        f = open(file_path , "r")
     #       contents = f.read()
      #      for import_statement in get_commons_imports(file_path):
       #         if import_statement[0].__contains__('ice_celery') or import_statement[1].__contains__('ice_celery') or\
        #                import_statement[0].__contains__('ice_rest') or import_statement[1].__contains__('ice_rest') :
         #           raise RuntimeError('ICE_COMMONS should not import any module from ICE_CELERY or ICE_REST. Please change the import {0} in file {1}'.format(import_statement, file_path))


