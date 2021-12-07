data = open('2021/5/input.txt', 'r').read().strip().split('\n')
for i, line in enumerate(data):
    data[i] = line.replace(' -> ', ',').split(',')
max_x = max([max(int(x[0]), int(x[2])) for x in data])
max_y = max([max(int(x[1]), int(x[3])) for x in data])
diagram = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for row in data:
    a, b, c, d = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    if a == c:
        if b > d:
            b, d = d, b
        for j in range(b, d + 1):
            diagram[j][a] += 1
    elif b == d:
        if a > c:
            a, c = c, a
        for j in range(a, c + 1):
            diagram[b][j] += 1
    elif (a > c) == (b > d):
        a, c = min(a, c), max(a, c)
        b, d = min(b, d), max(b, d)
        for j, k in zip(range(a, c + 1), range(b, d + 1)):
            diagram[k][j] += 1
    else:
        a, c = min(a, c), max(a, c)
        b, d = max(b, d), min(b, d)
        for j, k in zip(range(a, c + 1), range(b, d - 1, -1)):
            diagram[k][j] += 1
_sum = 0
for row in diagram:
    for point in row:
        if point >= 2:
            _sum += 1
print(_sum)