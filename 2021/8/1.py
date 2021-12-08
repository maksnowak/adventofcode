data = open('2021/8/input.txt', 'r').read().strip().split('\n')
digits = 0
for row in data:
    signals = row.split(' | ')
    for signal in signals[1].split(' '):
        if len(signal) == 2 or len(signal) == 3 or len(signal) == 4 or len(signal) == 7:
            digits += 1
print(digits)