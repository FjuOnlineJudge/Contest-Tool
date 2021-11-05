import argparse
import os
import shutil
import subprocess

parser = argparse.ArgumentParser(description='Generate tetsdata in selected folder')
parser.add_argument('folder', nargs='+', help='Folder name')
args = parser.parse_args()

for folder in args.folder:
    if not os.path.isdir('./%s'%(folder)):
        print('%s folder doesn\'t exist'%(folder))
        continue
    if not os.path.isfile('./%s/generate.py'%(folder)):
        print('There\'s no generate.py %s folder.'%(folder))
        continue
    os.chdir('./%s'%(folder))
    shutil.copy('./submissions/accepted/1.cpp', './AC.cpp')
    subprocess.call('g++ ./AC.cpp -o ./a.exe')
    subprocess.call('py ./generate.py')
    os.remove('./AC.cpp')
    os.remove('./a.exe')
    print('Already generate testdata in %s folder.'%(folder))
    os.chdir('..')