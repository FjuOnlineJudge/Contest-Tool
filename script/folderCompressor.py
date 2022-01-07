import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Compress problem folder', epilog='')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--domjudge', action='store_true', help='export to domjudge archive')
group.add_argument('-e', '--exclude', nargs= 1, help='select types to exclude (t: tex files, s: submissions, g: generate.py). (e.g. -e ts, -e g)')
parser.add_argument('folder', nargs='+', help='Folder name')
args = parser.parse_args()

excludeFile = '*.zip'

if args.domjudge:
    excludeFile = '*.tex generate.py'
elif args.exclude:
    str = args.exclude[0]
    for e in str:
        if e == 't':
            excludeFile = excludeFile + ' *.tex'
        elif e == 's':
            excludeFile = excludeFile + ' /submissions/*'
        elif e == 'g':
            excludeFile = excludeFile + ' generate.py'

for folder in args.folder:
    if not os.path.isdir('./%s'%(folder)):
        print('%s folder doesn\'t exist'%(folder))
        continue
    if os.path.isfile('./%s.zip'%(folder)):
        os.remove('./%s.zip'%(folder))
        print('%s.zip exists, remove it...'%(folder))
    os.chdir('./%s'%(folder))
    subprocess.call('zip %s.zip -r * -x %s'%(folder,excludeFile))
    os.chdir('..')
    os.rename('%s/%s.zip'%(folder,folder),'./%s.zip'%(folder))
    