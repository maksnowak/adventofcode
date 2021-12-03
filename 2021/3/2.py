with open('2021/3/input.txt', 'r') as f:
    oxygen = []
    co2 = []
    noOfZero = [0] * 12
    noOfOne = [0] * 12
    for line in f:
        oxygen.append(line.strip())
        co2.append(line.strip())
        i = 0
        for num in line.strip():
            if num == "0":
                noOfZero[i] += 1
            else:
                noOfOne[i] += 1
            i += 1
    oxygenRating = 0
    co2Rating = 0
    oxygenSearch = []
    co2Search = []
    for j in range(0, 10):
        if noOfOne[j] >= noOfZero[j]:
            oxygenSearch.append("1")
            co2Search.append("0")
        else:
            oxygenSearch.append("0")
            co2Search.append("1")
    k = 0
    for num in oxygenSearch:
        temp = []
        for line in oxygen:
            if line[k] == num:
                temp.append(line)
        oxygen = temp
        k += 1
    l = 0
    for num in co2Search:
        temp = []
        for line in co2:
            if line[l] == num:
                temp.append(line)
        co2 = temp
        l += 1

    print(oxygen)
    print(co2)
    print(int(oxygen[0], 2) * int(oxygen[0], 2))
        


    
print()