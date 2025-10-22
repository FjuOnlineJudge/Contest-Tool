import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Compress problem folder', epilog='')
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--all', action='store_true', help='compress all problem')
parser.add_argument('folders', nargs='*', help='The name of folders')
args = parser.parse_args()

def is_problem_dir(path: str) -> bool:
    if not os.path.isdir(path):
        return False
    
    start = ["abc", "arc", "agc", "cf", "hoj", "uva"]
    for word in start:
        if path.startswith(word):
            return True
    
    return False

if args.all:
    problem_dir = [path for path in os.listdir() if is_problem_dir(path)]
else:
    problem_dir = args.folders

for folder in problem_dir:
    print(f"Compress {folder}")
    if os.path.isfile('./%s.zip'%(folder)):
        os.remove('./%s.zip'%(folder))
        print('%s.zip exists, remove it...'%(folder))
    os.chdir('./%s'%(folder))
    subprocess.call(f'zip {folder}.zip -r * -x %s')
    os.chdir('..')
    os.rename('%s/%s.zip'%(folder,folder),'./%s.zip'%(folder))
    