import typing

numbers = ["0","1","2","3","4","5","6","7","8","9", "zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9, "zero":0,"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}


def find_calib_on_line_part_1(line: str) -> int:
    found_first = False
    found_last = False
    first_digit = -1
    last_digit = -1
    n = len(line)
    i = 0
    while i<n:
        if line[i] in numbers and not found_first:
            found_first = True
            first_digit = int(line[i])
        elif line[i] in numbers:
            found_last = True
            last_digit = int(line[i])
        i+=1

    if found_first and found_last:
        return first_digit*10+last_digit
    return first_digit*10+first_digit


def find_calib_on_line_part_2(line: str) -> int:
    found_first = False
    found_last = False
    first_digit = -1
    last_digit = -1
    n = len(line)
    first_digit_idx = n
    last_digit_idx = -1
    for i in list(numbers):
        idx = line.find(i)
        while idx!=-1:
            if idx<first_digit_idx:
                found_first = True
                first_digit_idx = idx
                first_digit = numbers_dict[i]
            if idx>last_digit_idx:
                found_last = True
                last_digit = numbers_dict[i]
                last_digit_idx = idx
            idx = line.find(i, idx+1, n)
    if found_first and found_last:
        return first_digit*10+last_digit
    return first_digit*10+first_digit


def calc_calib_part_1(file_path: str) -> int:
    with open(file_path) as file:
        res = 0
        for line in file.readlines():
            res+=find_calib_on_line_part_1(line)
        return res


def calc_calib_part_2(file_path: str) -> int:
    with open(file_path) as file:
        res = 0
        for line in file.readlines():
            res+=find_calib_on_line_part_2(line)
        return res


if __name__ == '__main__':
    file_path_data = r'C:\Users\noamo\Desktop\school\adventofcode\day1\data'
    file_path_example1 = r'C:\Users\noamo\Desktop\school\adventofcode\day1\example'
    file_path_example2= r'C:\Users\noamo\Desktop\school\adventofcode\day1\example2'
    assert (calc_calib_part_1(file_path_example1)==142)
    assert (calc_calib_part_2(file_path_example2)==281)
    assert (calc_calib_part_2(file_path_data)==54719)