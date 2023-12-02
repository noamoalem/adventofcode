import typing
from typing import Dict, Tuple
from collections import defaultdict

colors = {"red", "green", "blue"}


def parse_line(line: str):
    res = {"red": 0, "green": 0, "blue": 0}
    line = line.split(":")[1].strip()
    start_idx = 0
    semi_col_idx = line.find(";")
    while semi_col_idx != -1:
        curr_data = line[start_idx: semi_col_idx].strip().split(" ")
        idx = 0
        while idx < len(curr_data):
            if idx % 2 == 0:
                count = int(curr_data[idx])
            else:
                res[curr_data[idx].replace(",", "")] = max(count, res[curr_data[idx].replace(",", "")])
            idx += 1
        start_idx = semi_col_idx + 1
        semi_col_idx = line.find(";", semi_col_idx + 1)

    curr_data = line[start_idx:].strip().split(" ")
    idx = 0
    while idx < len(curr_data):
        if idx % 2 == 0:
            count = int(curr_data[idx])
        else:
            res[curr_data[idx].replace(",", "")] = max(count, res[curr_data[idx].replace(",", "")])
        idx += 1
    return res


def is_game_possible(game_num: int, game_data: str, game_rule) -> int:
    """
    This function check if a given game data is valid
    :param game_data:
    :param game_rule:
    :return: the game number if valid, 0 otherwise
    """
    d = parse_line(game_data)
    for c in colors:
        if d[c] > game_rule[c]:
            return 0
    return game_num


def found_valid_games(file_path: str, game_rule) -> int:
    with open(file_path, "r") as file:
        res = 0
        game_num = 1
        for line in file.readlines():
            res += is_game_possible(game_num, line, game_rule)
            game_num += 1
        return res


def calc_power_of_set_one_line(game_data: str) -> int:
    d = parse_line(game_data)
    res = 1
    for c in colors:
        res *= d[c]
    return res


def calc_power_of_set(file_path: str) -> int:
    with open(file_path, "r") as file:
        res = 0
        for line in file.readlines():
            res += calc_power_of_set_one_line(line)
        return res


if __name__ == '__main__':
    assert (found_valid_games(r'C:\Users\noamo\Desktop\school\adventofcode\day2\data',
                              {"red": 12, "green": 13, "blue": 14}) == 3059)
    assert (found_valid_games(r'C:\Users\noamo\Desktop\school\adventofcode\day2\example',
                              {"red": 12, "green": 13, "blue": 14}) == 8)
    assert (calc_power_of_set(r'C:\Users\noamo\Desktop\school\adventofcode\day2\example') == 2286)
    assert (calc_power_of_set(r'C:\Users\noamo\Desktop\school\adventofcode\day2\data') == 65371)
