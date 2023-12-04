def find_one_game_points(line: str) -> int:
    """
    This function calc the point of a given game. the rules are the first match makes the card
    worth one point and each match after the first doubles the point value of that card.
    :param line: a given game.
    :return: the point of a given game card.
    """

    line = line.split(":")[1]
    winning_numbers = line.split("|")[0].strip().split(" ")
    my_numbers = line.split("|")[1].strip().split(" ")
    winning_numbers = [int(i) for i in winning_numbers if i.isdigit()]
    my_numbers = [int(i) for i in my_numbers if i.isdigit()]

    res = 0
    for n in my_numbers:
        if n in winning_numbers:
            if not res:
                res = 1
            else:
                res *= 2
    return res


def find_scratchcards_points(file_path) -> int:
    """
    This function calc the point of all the game card. The rules are the first match makes the card
    worth one point and each match after the first doubles the point value of that card.
    :param file_path: all game cards data.
    :return: the sum of point of all the game card.
    """

    with open(file_path, 'r') as file:
        res = 0
        for line in file.readlines():
            res += find_one_game_points(line)
        return res


def count_matches_numbers_one_line(line: str) -> int:
    """
    This function calc the number of matching numbers in a given game.
    :param line: a given game.
    :return: the number of matching numbers in the given game.
    """
    line = line.split(":")[1]
    winning_numbers = line.split("|")[0].strip().split(" ")
    my_numbers = line.split("|")[1].strip().split(" ")

    winning_numbers = [int(i) for i in winning_numbers if i.isdigit()]
    my_numbers = [int(i) for i in my_numbers if i.isdigit()]

    count_matches = 0
    for n in my_numbers:
        if n in winning_numbers:
            count_matches += 1
    return count_matches


def find_all_copies(file_path) -> int:
    """
    This function cala the number of copies of all the game cards.
    :param file_path: all game cards data.
    :return: the number of copies of all the game cards.
    """

    with open(file_path, 'r') as file:
        lines = file.readlines()
        copies_d = {}
        for i in range(1, len(lines) + 1):
            copies_d[i] = 1
        game_num = 1
        res = 0
        for line in lines:
            res = count_matches_numbers_one_line(line)
            for i in range(game_num + 1, res + game_num + 1):
                if i in copies_d:
                    copies_d[i] += 1 * copies_d[game_num]
                else:
                    copies_d[i] = 1 + 1 * copies_d[game_num]
            game_num += 1
        return sum(copies_d.values())


if __name__ == '__main__':
    assert (find_scratchcards_points(r'C:\Users\noamo\Desktop\school\adventofcode\day4\example') == 13)
    assert (find_scratchcards_points(r'C:\Users\noamo\Desktop\school\adventofcode\day4\data') == 25174)
    assert (find_all_copies(r'C:\Users\noamo\Desktop\school\adventofcode\day4\example') == 30)
    assert (find_all_copies(r'C:\Users\noamo\Desktop\school\adventofcode\day4\data') == 6420979)
