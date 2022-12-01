def firstPuzzle(file):
    data = open(file, 'r').read().strip().split('\n\n')
    sums = []
    for elf in data:
        all_calories = 0
        for food in elf.split('\n'):
            all_calories += int(food)
        sums.append(all_calories)
    return max(sums)


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

print(firstPuzzle('2022/1/example.txt'))
print(firstPuzzle('2022/1/input.txt'))

print(secondPuzzle('2022/1/example.txt'))
print(secondPuzzle('2022/1/input.txt'))
