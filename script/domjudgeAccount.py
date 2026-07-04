import argparse
import random
import string
from enum import Enum

class Team(Enum):
    ID = 0
    DISPLAY_NAME = 1
    ACCONUT = 2
    PASSWORD = 3


def read_team_name(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf8") as input_file:
        team_name: list[str] = [line.replace('\n', '') for line in input_file.readlines()]
    
    return team_name


def generate_password(length: int = 8) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def generate_team(team_name: list[str], number: int) -> list[list[str]]:
    # return: id, display name, account, password
    team: list[str] = []
    for name in team_name:
        team.append([number, name, f"team{number}", generate_password(8)])
        number += 1
    
    return team


def generate_team_tsv(team: list[list[str]]) -> None:
    with open("team.tsv", "w") as output_file:
        output_file.write("teams\t1\n")
        for t in team:
            output_file.write(f"{t[Team.ID.value]}\t\t{5}\t{t[Team.DISPLAY_NAME.value]}\n")


def generate_account_tsv(team: list[list[str]]) -> None:
    with open("account.tsv", "w") as output_file:
        output_file.write("accounts\t1\n")
        for t in team:
            output_file.write(f"team\t{t[Team.DISPLAY_NAME.value]}\t{t[Team.ACCONUT.value]}\t{t[Team.PASSWORD.value]}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description='Compress problem folder', epilog='')
    parser.add_argument('-f', '--filename', help='team txt file')
    parser.add_argument('-n', '--number', type=int, help='which number to start')
    args = parser.parse_args()
    
    team_name = read_team_name(args.filename)
    team = generate_team(team_name, args.number)
    
    generate_team_tsv(team)
    generate_account_tsv(team)
    

if __name__ == "__main__":
    main()