def firstPuzzle(file):
    data = open(file, 'r').read().strip()
    for i in range(4, len(data)):
        marker = data[i-4:i]
        if sorted(marker) == list(sorted(set(marker))):
            return i


def secondPuzzle(file):
    data = open(file, 'r').read().strip()
    for i in range(14, len(data)):
        marker = data[i-14:i]
        if sorted(marker) == list(sorted(set(marker))):
            return i


print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
