from typing import List


def check_is_a_part_number(schematic_file_mat: List[List[str]], num_len:int, num_end_col_idx:int , num_row_idx:int):
    for d in [-1, 1]:
        i = num_row_idx
        j = num_end_col_idx - num_len
        if j > 0:
            j -= 1
        if num_row_idx+d >=0 and num_row_idx+d < len(schematic_file_mat):
            i +=d
            while j<=num_end_col_idx and j<len(schematic_file_mat[0]):
                if not schematic_file_mat[i][j].isdigit() and not schematic_file_mat[i][j] == '.':
                    return True
                j+=1
    j = num_end_col_idx
    if j<len(schematic_file_mat[0]):
        if not schematic_file_mat[num_row_idx][j].isdigit() and not schematic_file_mat[num_row_idx][j] == '.':
            return True
    j = num_end_col_idx-num_len
    if j>0:
        j-=1
        if not schematic_file_mat[num_row_idx][j].isdigit() and not schematic_file_mat[num_row_idx][j] == '.':
            return True
    return False


def check_is_adjacent_to_star(schematic_file_mat: List[List[str]], num_len:int, num_end_col_idx:int , num_row_idx:int):
    for d in [-1, 1]:
        i = num_row_idx
        j = num_end_col_idx - num_len
        if j > 0:
            j -= 1
        if num_row_idx+d >=0 and num_row_idx+d < len(schematic_file_mat):
            i +=d
            while j<=num_end_col_idx and j<len(schematic_file_mat[0]):
                if schematic_file_mat[i][j] == '*':
                    return i,j
                j+=1
    j = num_end_col_idx
    if j<len(schematic_file_mat[0]):
        if schematic_file_mat[num_row_idx][j] == '*':
            return num_row_idx, j
    j = num_end_col_idx-num_len
    if j>0:
        j-=1
        if schematic_file_mat[num_row_idx][j] == '*':
            return num_row_idx, j
    return -1,-1


def sum_all_adjacent_symbol(schematic_file_mat):
    i, j = 0, 0
    res = 0
    while i<len(schematic_file_mat):
        j =0
        while j<len(schematic_file_mat[0]):
            curr_num = 0
            num_len = 0
            while j<len(schematic_file_mat[0])and schematic_file_mat[i][j].isdigit():
                curr_num = curr_num*10 + int(schematic_file_mat[i][j])
                num_len+=1
                j+=1
            if num_len and check_is_a_part_number(schematic_file_mat, num_len, j, i):
                # print(curr_num)
                res+=curr_num
            j+=1
        i+=1
    return res


def sum_all_gears(schematic_file_mat):
    i, j = 0, 0
    res = 0
    star_d = {}
    while i<len(schematic_file_mat):
        j =0
        while j<len(schematic_file_mat[0]):
            curr_num = 0
            num_len = 0
            while j<len(schematic_file_mat[0]) and schematic_file_mat[i][j].isdigit():
                curr_num = curr_num*10 + int(schematic_file_mat[i][j])
                num_len+=1
                j+=1
            if num_len:
                x,y =  check_is_adjacent_to_star(schematic_file_mat, num_len, j, i)
                if x!=-1 and y!=-1:
                    if (x,y) in star_d:
                        star_d[(x,y)].append(curr_num)
                    else:
                        star_d[(x, y)] = [curr_num]
            j+=1
        i+=1
    values = star_d.values()
    for v in values:
        if len(v) == 2:
            res+= v[0]*v[1]
    return res


def read_engine_schematic_file_to_mat(file_path: str):
    with open(file_path, 'r') as file:
        res = []
        for line in file.readlines():
            res.append([*line.strip()])
        return res


if __name__ == '__main__':
    file_data = r'C:\Users\noamo\Desktop\school\adventofcode\day3\data'
    file_example = r'C:\Users\noamo\Desktop\school\adventofcode\day3\example'
    file_example_mat = read_engine_schematic_file_to_mat(file_example)
    file_data_mat = read_engine_schematic_file_to_mat(file_data)
    assert (sum_all_adjacent_symbol(file_example_mat)==4361)
    assert (sum_all_adjacent_symbol(file_data_mat)==525119)
    assert(sum_all_gears(file_example_mat)==467835)
    assert (sum_all_gears(file_data_mat) == 76504829)