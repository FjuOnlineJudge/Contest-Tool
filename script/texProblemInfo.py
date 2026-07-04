import os
import re

def parse_ini(file_path):
    """Parse domjudge-problem.ini to extract name and timelimit"""
    name, timelimit = None, None
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("name"):
                match = re.search(r'name\s*=\s*["\']?(.*?)["\']?$', line)
                if match:
                    name = match.group(1)
            elif line.startswith("timelimit"):
                match = re.search(r'timelimit\s*=\s*["\']?(.*?)["\']?$', line)
                if match:
                    timelimit = match.group(1)
    return name, timelimit

def is_problem_dir(path: str) -> bool:
    if not os.path.isdir(path):
        return False
    
    start = ["abc", "arc", "agc", "cf", "hoj", "uva"]
    for word in start:
        if path.startswith(word):
            return True
    
    return False

def main():
    for path in os.listdir("."):
        if is_problem_dir(path):
            ini_path = os.path.join(path, "domjudge-problem.ini")
            if os.path.exists(ini_path):
                name, timelimit = parse_ini(ini_path)
                if name and timelimit:
                    print(f"\\problem{{{path}}}{{{name}}}{{{timelimit}}}{{2048}}")

if __name__ == "__main__":
    main()
