def firstPuzzle(file):
    data = open(file, 'r').read().strip().split('\n')
    sum_of_priorities = 0
    for rugsack in data:
        item_in_both = None
        compartments = [rugsack[:len(rugsack) // 2], rugsack[len(rugsack) // 2:]]
        for item in compartments[0]:
            if item in list(compartments[1]):
                item_in_both = item
                if item_in_both.isupper():
                    sum_of_priorities += ord(item_in_both) - 38
                else:
                    sum_of_priorities += ord(item_in_both) - 96
                break
    return sum_of_priorities


def secondPuzzle(file):
    data = open(file, 'r').read().strip().split('\n')
    sum_of_priorities = 0
    for i in range(0, len(data)-2, 3):
        item_in_all = None
        rugsacks = data[i:i+3]
        for item in rugsacks[0]:
            if all([item in rugsacks[1], item in rugsacks[2]]):
                item_in_all = item
                if item_in_all.isupper():
                    sum_of_priorities += ord(item_in_all) - 38
                else:
                    sum_of_priorities += ord(item_in_all) - 96
                break
    return sum_of_priorities


print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
