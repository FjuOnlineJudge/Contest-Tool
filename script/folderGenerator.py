import argparse
import os
import shutil

archive_folder = "./_archive"

parser = argparse.ArgumentParser(description='Generate problem folder')
parser.add_argument('pid', nargs='+', help='Problem ID')
parser.add_argument('-s', '--sample', type=int, default=1, help='The number of sample case')
parser.add_argument('-j', '--spj', action='store_true', help='Whether to use speical judge')
args = parser.parse_args()

for pid in args.pid:    
    if os.path.isdir(f"./{pid}"):
        print(f"{pid} folder exists")
        continue

    if os.path.exists(f"{archive_folder}/{pid}.zip"):
        print(f"{pid}.zip exists")
        shutil.unpack_archive(f"{archive_folder}/{pid}.zip", pid)
        print(f"{pid}.zip have been compressed ")
        continue

    # copy sample file
    shutil.copytree(f"./template/sample", f"./{pid}")

    # create testdata folder
    for subfolder in ["data", "data/sample", "/data/secret"]:
        os.mkdir(f"{pid}/{subfolder}")

    for i in range(1, args.sample + 1):
        open(f"{pid}/data/sample/{i}.in", "w")
        open(f"{pid}/data/sample/{i}.ans", "w")

    # copy submissions folder
    os.mkdir(f"{pid}/submissions")
    os.mkdir(f"{pid}/submissions/accepted")

    # copy special judge folder
    if args.spj:
        shutil.copytree(f"./template/output_validators", f"./{pid}/output_validators")

    print(f"{pid} has generated")