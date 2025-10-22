import argparse
import os
import shutil
import subprocess

parser = argparse.ArgumentParser(description="Generate tetsdata in selected folder")
parser.add_argument("folder", help="Folder name")
args = parser.parse_args()

for folder in args.folder:
    if not os.path.isdir(f"./{folder}"):
        print(f"{folder} folder doesn\"t exist")
        continue

    if not os.path.isfile(f"./{folder}/generate.py"):
        print(f"There\"s no generate.py {folder} folder.")
        continue

    os.chdir(f"./{folder}")
    shutil.copy("./submissions/accepted/1.cpp", "./AC.cpp")
    subprocess.call("g++ ./AC.cpp -o ./a.exe", shell=True)
    subprocess.call("python ./generate.py", shell=True)
    os.remove("./AC.cpp")
    os.remove("./a.exe")
    print(f"Already generate testdata in {folder} folder.")
    os.chdir("..")