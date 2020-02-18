'''
python script to automate mitie build creattion and installation of mitie in given virtual environment path.
'''

import os
import sys
import glob
import shutil
import git

#current_working_dir = os.getcwd()
current_working_dir = os.path.expanduser('~')

# get input
#virtual_env_path = raw_input("give local virtual environment path")
#git_url = raw_input("give git url")
virtual_env_path = sys.argv[1]
git_url = sys.argv[2]


print("mitie installation start.")

if os.path.exists(current_working_dir+os.sep+'mitie'):
    shutil.rmtree(current_working_dir+os.sep+'mitie')

# clone git
git.Git(current_working_dir).clone(git_url)

# change directory to mitie
os.chdir(current_working_dir+os.sep+'mitie')

# build mitie
os.system('python setup.py build')

# copy file from build to python sitepackages.
root_src_dir = current_working_dir+os.sep+'mitie' + os.sep + 'build/lib/mitie'
root_target_dir = virtual_env_path + os.sep + 'local/lib/python2.7/site-packages/mitie'

operation= 'copy' # 'copy' or 'move'

if os.path.exists(root_target_dir):
    shutil.rmtree(root_target_dir)

if not os.path.exists(root_src_dir):
    if len(glob.glob(current_working_dir + os.sep + 'mitie' + os.sep + 'build/lib*')) > 0:
        old_filename = glob.glob(current_working_dir + os.sep + 'mitie' + os.sep + 'build/lib*')[0]
        new_filename = current_working_dir + os.sep + 'mitie' + os.sep + 'build/lib'
        os.rename(old_filename, new_filename)
    else:
        raise Exception("please check build happened or not !!. bcs i am not able to find build/lib directory.")

if operation is 'copy':
    shutil.copytree(root_src_dir, root_target_dir)

print("mitie installation completed.")
