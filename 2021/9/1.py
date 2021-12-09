data = open('2021/9/input.txt').read().strip().split('\n')
for i, row in enumerate(data):
    data[i] = [int(x) for x in row]
low = []
for i, row in enumerate(data):
    for j, height in enumerate(row):
        left = False
        right = False
        top = False
        bottom = False
        try:
            if data[i][j] < data[i][j - 1]:
                left = True
        except:
            left = True
        try:
            if data[i][j] < data[i][j + 1]:
                right = True
        except:
            right = True
        try:
            if data[i][j] < data[i - 1][j]:
                top = True
        except:
            top = True
        try:
            if data[i][j] < data[i + 1][j]:
                bottom = True
        except:
            bottom = True
        if left and right and top and bottom:
            low.append(int(height))
risk = [1 + x for x in low]
print(sum(risk))