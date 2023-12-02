import typing
from typing import Dict, Tuple
from collections import defaultdict

colors = {"red", "green", "blue"}


def parse_line(line: str):
    """
    This function parse a line of one game data.
    :param line: a given game data.
    :return: a dict with the minimum number of ball needed for the given game.
    """
    res = {"red": 0, "green": 0, "blue": 0}
    line = line.split(":")[1].strip()
    start_idx = 0
    semi_col_idx = line.find(";")
    while semi_col_idx != -1:
        semi_col_idx, start_idx = parse_one_set(line, res, semi_col_idx, start_idx)
    curr_data = line[start_idx:].strip().split(" ")
    idx = 0
    semi_col_idx, start_idx = parse_one_set(line, res, len(line), start_idx)
    return res


def parse_one_set(line, res, semi_col_idx, start_idx):
    """
    This function parse one set in a game.
    :param line: a given game data.
    :param res: a dict with the minimum number of ball needed for the given game.
    :param semi_col_idx: the end of the set data in the given line
    :param start_idx: the start of the set data in the given line
    :return: the start and end index for the next set.
    """
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
    return semi_col_idx, start_idx


def is_game_possible(game_num: int, game_data: str, game_rule) -> int:
    """
    This function check if a given game data is valid.
    :param game_data: a given game data.
    :param game_rule: the ruls for the game.
    :return: the game number if valid, 0 otherwise.
    """
    d = parse_line(game_data)
    for c in colors:
        if d[c] > game_rule[c]:
            return 0
    return game_num


def found_valid_games(file_path: str, game_rule) -> int:
    """
    This function sum all the valid game nummbers.
    :param file_path: path of the file.
    :param game_rule: the ruls for the game.
    :return: the sum of all the valid game numbers.
    """
    with open(file_path, "r") as file:
        res = 0
        game_num = 1
        for line in file.readlines():
            res += is_game_possible(game_num, line, game_rule)
            game_num += 1
        return res


def calc_power_of_set_one_line(game_data: str) -> int:
    """

    :param game_data: a given game data.
    :return:
    """
    d = parse_line(game_data)
    res = 1
    for c in colors:
        res *= d[c]
    return res


def calc_power_of_set(file_path: str) -> int:
    """

    :param file_path: path of the file.
    :return:
    """
    with open(file_path, "r") as file:
        res = 0
        for line in file.readlines():
            res += calc_power_of_set_one_line(line)
        return res


if __name__ == '__main__':
    assert (found_valid_games(r'C:\Users\noamo\Desktop\school\adventofcode\day2\example',
                              {"red": 12, "green": 13, "blue": 14}) == 8)
    assert (found_valid_games(r'C:\Users\noamo\Desktop\school\adventofcode\day2\data',
                              {"red": 12, "green": 13, "blue": 14}) == 3059)
    assert (calc_power_of_set(r'C:\Users\noamo\Desktop\school\adventofcode\day2\example') == 2286)
    assert (calc_power_of_set(r'C:\Users\noamo\Desktop\school\adventofcode\day2\data') == 65371)
