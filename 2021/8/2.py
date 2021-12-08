data = open('2021/8/input.txt', 'r').read().strip().split('\n')
_sum = 0
for row in data:
    signals = row.split(' | ')
    zero, one, two, three, four, five, six, seven, eight, nine = None, None, None, None, None, None, None, None, None, None
    lenfive, lensix = [], []
    for signal in signals[0].split(' '):
        if len(signal) == 2:
            one = signal
        elif len(signal) == 3:
            seven = signal
        elif len(signal) == 4:
            four = signal
        elif len(signal) == 7:
            eight = signal
        elif len(signal) == 5:
            lenfive.append(signal)
        elif len(signal) == 6:
            lensix.append(signal)
    for num in lenfive:
        if len(set(list(four)).intersection(list(num))) == 3 and len(set(list(one)).intersection(list(num))) == 2:
            three = num
        elif len(set(list(four)).intersection(list(num))) == 3 and len(set(list(one)).intersection(list(num))) == 1:
            five = num
        else:
            two = num
    for num in lensix:
        if len(set(list(four)).intersection(list(num))) == 3 and len(set(list(one)).intersection(list(num))) == 2:
            zero = num
        elif len(set(list(four)).intersection(list(num))) == 4 and len(set(list(one)).intersection(list(num))) == 2:
            nine = num
        else:
            six = num
    number = ""
    for signal in signals[1].split(' '):
        if ''.join(sorted(signal)) == ''.join(sorted(zero)):
            number += "0"
        elif ''.join(sorted(signal)) == ''.join(sorted(one)):
            number += "1"
        elif ''.join(sorted(signal)) == ''.join(sorted(two)):
            number += "2"
        elif ''.join(sorted(signal)) == ''.join(sorted(three)):
            number += "3"
        elif ''.join(sorted(signal)) == ''.join(sorted(four)):
            number += "4"
        elif ''.join(sorted(signal)) == ''.join(sorted(five)):
            number += "5"
        elif ''.join(sorted(signal)) == ''.join(sorted(six)):
            number += "6"
        elif ''.join(sorted(signal)) == ''.join(sorted(seven)):
            number += "7"
        elif ''.join(sorted(signal)) == ''.join(sorted(eight)):
            number += "8"
        elif ''.join(sorted(signal)) == ''.join(sorted(nine)):
            number += "9"
    _sum += int(number)
print(_sum)