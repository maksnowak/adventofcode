with open('2021/1/input.txt', 'r') as f:
    noOfIncreased = 0
    lines = []
    for line in f:
        lines.append(int(line.strip()))
    prev = sum(lines[0:3])
    for i in range(1, len(lines) - 2):
        if sum(lines[i:i+3]) > prev:
            noOfIncreased += 1
        prev = sum(lines[i:i+3])
    print(noOfIncreased)