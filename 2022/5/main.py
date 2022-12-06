#TODO make the program work with a standard input, not a modified one (see README.md)
def firstPuzzle(file):
    data = open(file).read().split('\n\n')
    crates = data[0]
    instructions = data[1].strip().split('\n')
    crates_list = crates.split('\n')
    final_list = [list(line[1::4]) for line in crates_list[:-1]]
    stacks = []
    for i in range(len(final_list[0])):
        stack = []
        for j in range(len(final_list)):
            try:
                if final_list[-1-j][i] != ' ':
                    stack.append(final_list[-1-j][i])
            except:
                pass
        stacks.append(stack)
    for instruction in instructions:
        instruction_list = instruction.split(' ')
        to_be_moved = stacks[int(instruction_list[3]) - 1][int(instruction_list[1])*(-1):]
        for _ in range(int(instruction_list[1])):
            stacks[int(instruction_list[3]) - 1].pop()
        for item in to_be_moved[-1::-1]:
            stacks[int(instruction_list[5]) - 1].append(item)
    string = ""
    for stack in stacks:
        string += stack[-1]
    return string

def secondPuzzle(file):
    data = open(file).read().split('\n\n')
    crates = data[0]
    instructions = data[1].strip().split('\n')
    crates_list = crates.split('\n')
    final_list = [list(line[1::4]) for line in crates_list[:-1]]
    stacks = []
    for i in range(len(final_list[0])):
        stack = []
        for j in range(len(final_list)):
            try:
                if final_list[-1-j][i] != ' ':
                    stack.append(final_list[-1-j][i])
            except:
                pass
        stacks.append(stack)
    for instruction in instructions:
        instruction_list = instruction.split(' ')
        to_be_moved = stacks[int(instruction_list[3]) - 1][int(instruction_list[1])*(-1):]
        for _ in range(int(instruction_list[1])):
            stacks[int(instruction_list[3]) - 1].pop()
        for item in to_be_moved:
            stacks[int(instruction_list[5]) - 1].append(item)
    string = ""
    for stack in stacks:
        string += stack[-1]
    return string


print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
