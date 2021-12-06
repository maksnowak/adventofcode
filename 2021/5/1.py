data = open('2021/5/testinput.txt', 'r').read().split('\n')
for i, line in enumerate(data):
    data[i] = line.split(' -> ')
data.pop()
diagram_row = [0] * len(data)
diagram = [diagram_row] * len(data)
print(data)
print(diagram)
for row in data:
    a = row[0].split(',')
    b = row[1].split(',')
    if a[0] == b[0]:
        c = int(a[1])
        d = int(b[1])
        if c > d:
            temp = c
            c = d
            d = temp
        for j in range(c, d + 1):
            diagram[j][int(a[0])] += 1
    elif a[1] == b[1]:
        c = int(a[0])
        d = int(b[0])
        if c > d:
            temp = c
            c = d
            d = temp
        for j in range(c, d + 1):
            diagram[int(a[1])][j] += 1
    else:
        pass
print(diagram)
