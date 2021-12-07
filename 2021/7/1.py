data = [int(x) for x in open('2021/7/input.txt', 'r').read().strip().split(',')]
cheapest = None
for position in range(max(data)):
    _sum = 0
    for num in data:
        _sum += abs(position - num)
    if cheapest == None:
        cheapest = _sum
    elif _sum < cheapest:
        cheapest = _sum
print(cheapest)