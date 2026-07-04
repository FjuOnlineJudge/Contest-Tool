import argparse
import subprocess
import os
import zipfile

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

    zip_path = f'./{folder}.zip'

    # 如果 zip 已存在就刪除
    if os.path.isfile(zip_path):
        os.remove(zip_path)
        print(f'{folder}.zip exists, remove it...')

    folder_path = f'./{folder}'

    # 建立 zip
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)

                # 排除 zip 本身（避免重複壓縮）
                if full_path.endswith('.zip'):
                    continue

                # 壓縮時的相對路徑（避免帶入 ./folder）
                arcname = os.path.relpath(full_path, folder_path)

                zf.write(full_path, arcname)
    