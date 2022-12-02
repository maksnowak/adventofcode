def compare_first(shapes):
    if any([shapes == ['A', 'X'], shapes == ['B', 'Y'], shapes == ['C', 'Z']]):
        return 3
    elif any([shapes == ['C', 'X'], shapes == ['B', 'Z'], shapes == ['A', 'Y']]):
        return 6
    else:
        return 0


def compare_second(shapes):
    if shapes[1] == 'X':
        if shapes[0] == 'A':
            return 3
        elif shapes[0] == 'B':
            return 1
        else:
            return 2
    elif shapes[1] == 'Y':
        if shapes[0] == 'A':
            return 1
        elif shapes[0] == 'B':
            return 2
        else:
            return 3
    else:
        if shapes[0] == 'A':
            return 2
        elif shapes[0] == 'B':
            return 3
        else:
            return 1


def firstPuzzle(file):
    data = open(file, 'r').read().strip().split('\n')
    response = {'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for line in data:
        shapes = line.split()
        score += compare_first(shapes) + response[shapes[1]]
    return score


def secondPuzzle(file):
    data = open(file, 'r').read().strip().split('\n')
    response = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0
    for line in data:
        shapes = line.split()
        score += compare_second(shapes) + response[shapes[1]]
    return score


print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
