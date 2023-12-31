import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Generate problem folder')
parser.add_argument('folder', nargs='+', help='Folder name')
args = parser.parse_args()

for folder in args.folder:
    if os.path.isdir("./%s"%(folder)):
        print("%s already exists"%(folder))
        continue
    shutil.copytree("./sample", "./%s"%(folder))
    os.mkdir("./%s/data"%(folder))
    os.mkdir("./%s/data/sample"%(folder))
    open("./%s/data/sample/1.in"%(folder), "w")
    open("./%s/data/sample/1.ans"%(folder), "w")
    os.mkdir("./%s/data/secret"%(folder))
    os.mkdir("./%s/submissions"%(folder))
    os.mkdir("./%s/submissions/accepted"%(folder))
    print("%s has generated"%(folder))