

def perform_instructions(instructions, steps):
    count = 0
    curr_node = 'AAA'
    i = 0
    while i < len(instructions):
        if instructions[i] == 'L':
            idx = 0
        else:
            idx = 1
        curr_node = steps[curr_node][idx]
        count+=1
        if curr_node == 'ZZZ':
            return count
        i+=1
        if i == len(instructions):
            i = 0


def perform_instructions_part_2(instructions, steps):
    count = 0
    curr_nodes = [n for n in steps.keys() if n.endswith('A')]
    i = 0
    while i < len(instructions):
        if instructions[i] == 'L':
            idx = 0
        else:
            idx = 1
        for n in range(len(curr_nodes)):
            curr_nodes[n] = steps[curr_nodes[n]][idx]
        count+=1
        is_all_z = [n.endswith("Z") for n in curr_nodes]
        if all(is_all_z):
            return count
        i+=1
        if i == len(instructions):
            print("here")
            i = 0


def read_instructions_and_steps(file_path):
    with open(file_path, 'r') as file:
        all_lines = file.readlines()
        instructions = all_lines[0]
        steps = {}
        for l in all_lines[2:]:
            data = l.split("=")
            data[1] = data[1].replace("(", "")
            data[1] = data[1].replace(")", "")
            data[1] = data[1].replace(",", "")
            steps[data[0].strip()] = data[1].strip().split(" ")
        return instructions.strip(), steps


if __name__ == '__main__':
    example_path = r'example'
    example2_path = r'example2'
    data_path = r'data'
    instructions, steps = read_instructions_and_steps(example2_path)
    # assert (perform_instructions(instructions, steps)==6)
    # print(perform_instructions(instructions, steps))
    assert (perform_instructions_part_2(instructions, steps)==6)
    print (perform_instructions_part_2(instructions, steps))
