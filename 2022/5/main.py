#TODO make the program work with a standard input, not a modified one (see README.md)
def firstPuzzle(file):
    data = open(file).read().strip().split('\n\n')
    crates = data[0].split('\n')
    instructions = data[1]
    crates_list = []
    for stack in crates:
        stripped = stack[1:-1]
        crates_list.append(stripped.split(']['))
    for instruction in instructions.split('\n'):
        instruction_list = instruction.split(' ')
        to_be_moved = crates_list[int(instruction_list[3]) - 1][int(instruction_list[1])*(-1):]
        for _ in range(int(instruction_list[1])):
            crates_list[int(instruction_list[3]) - 1].pop()
        for item in to_be_moved[-1::-1]:
            crates_list[int(instruction_list[5]) - 1].append(item)
    string = ""
    for stack in crates_list:
        string += stack[-1]
    return string


def secondPuzzle(file):
    data = open(file).read().strip().split('\n\n')
    crates = data[0].split('\n')
    instructions = data[1]
    crates_list = []
    for stack in crates:
        stripped = stack[1:-1]
        crates_list.append(stripped.split(']['))
    for instruction in instructions.split('\n'):
        instruction_list = instruction.split(' ')
        to_be_moved = crates_list[int(instruction_list[3]) - 1][int(instruction_list[1])*(-1):]
        for _ in range(int(instruction_list[1])):
            crates_list[int(instruction_list[3]) - 1].pop()
        for item in to_be_moved:
            crates_list[int(instruction_list[5]) - 1].append(item)
    string = ""
    for stack in crates_list:
        string += stack[-1]
    return string


print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
