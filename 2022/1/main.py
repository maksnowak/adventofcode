def firstPuzzle(file):
    data = open(file, 'r').read().strip().split('\n\n')
    sums = []
    for elf in data:
        all_calories = 0
        for food in elf.split('\n'):
            all_calories += int(food)
        sums.append(all_calories)
    return max(sums)
    data.close()


def secondPuzzle(file):
    data = open(file, 'r').read().strip().split('\n\n')
    sums = []
    for elf in data:
        all_calories = 0
        for food in elf.split('\n'):
            all_calories += int(food)
        sums.append(all_calories)
    sums.sort()
    top_three = sums[-3:]
    sum_of_three = sum(top_three)
    return sum_of_three
    data.close()

print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
