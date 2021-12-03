with open('2021/3/input.txt', 'r') as f:
    noOfZero = [0] * 12
    noOfOne = [0] * 12
    gamma = ""
    for line in f:
        i = 0
        for num in line.strip():
            if num == "0":
                noOfZero[i] += 1
            else:
                noOfOne[i] += 1
            i += 1
    for i in range (0, 12):
        if noOfZero[i] > noOfOne[i]:
            gamma += "0"
        else:
            gamma += "1"
    epsilon = ""
    for num in gamma:        
        if num =="0":
            epsilon += "1"
        else:
            epsilon += "0"
print(int(gamma, 2) * int(epsilon, 2))