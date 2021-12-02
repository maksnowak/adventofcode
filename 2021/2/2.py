with open('2021/2/input.txt', 'r') as f:
    depth = 0
    position = 0
    aim = 0
    for line in f:
        course = line.strip().split()
        if course[0] == "forward":
            position += int(course[1])
            depth += aim * int(course[1])
        elif course[0] == "down":
            aim += int(course[1])
        elif course[0] == "up":
            aim -= int(course[1])

    print(position * depth)