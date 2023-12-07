from itertools import groupby
strength = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}

def find_score(hand_lines):
    res = []
    for line in hand_lines:
        hand, bid = line.split(" ")
        res.append([score(hand), ['23456789TJQKA'.index(c) + 1 for c in hand],hand,int(bid)])
    res.sort(key=lambda x: x[0])
    ranked_groups = [list(g) for _, g in groupby(res, lambda x: x[0])]
    for r in ranked_groups:
        r.sort(key=lambda x: x[1])

    groups = []
    for g in ranked_groups:
        groups += g
    return groups

def score(hand):
    s = sorted(hand)
    if len(set(s)) == 1:
        return 7
    elif s[0] == s[1] == s[2] == s[3] or s[1] == s[2] == s[3] == s[4]:
        return 6
    elif s[0] == s[1] == s[2] and s[3] == s[4] or s[0] == s[1] and s[2] == s[3] == s[4]:
        return 5
    elif s[0] == s[1] == s[2] or s[1] == s[2] == s[3] or s[2] == s[3] == s[4]:
        return 4
    elif s[0] == s[1] and s[2] == s[3] or s[0] == s[1] and s[3] == s[4] or s[1] == s[2] and s[3] == s[4]:
        return 3
    elif len(set(s)) == 4:
        return 2
    elif len(set(s)) == 5:
        return 1

def calc_total_winnings(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rank_list = find_score(lines)
        print(rank_list)
        n = len(lines)
        res = 0
        for i in range(1, n+1):
            print(rank_list[i-1][3], i)
            res += rank_list[i-1][3]*i

        return res

if __name__ == '__main__':
    data_path = r"C:\Users\noamo\Desktop\school\adventofcode\day7\data"
    example_path = r"C:\Users\noamo\Desktop\school\adventofcode\day7\example"

    assert (calc_total_winnings(example_path)==6440)
    print(calc_total_winnings(data_path))