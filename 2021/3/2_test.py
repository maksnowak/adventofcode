with open('2021/3/testinput.txt', 'r') as f:
    oxygen = []
    co2 = []
    for line in f:
        oxygen.append(line.strip())
        co2.append(line.strip())
    for j in range(5):
        oxygenSearch = []
        co2Search = []
        for i in range(len(oxygen)):
            for num in f.readlines():
                if num == "0":
                    noOfZero[i] += 1
                else:
                    noOfOne[i] += 1
                i += 1
        noOfZero = [0] * 5
        noOfOne = [0] * 5
        if noOfOne[j] >= noOfZero[j]:
            oxygenSearch.append("1")
        else:
            oxygenSearch.append("0")
        if noOfOne[j] <= noOfZero[j]:
            co2Search.append("1")
        else:
            co2Search.append("0")
        k = 0
        for num in oxygenSearch:
            if len(oxygen) != 1:
                temp = []
                for element in oxygen:
                    if element[k] == num:
                        temp.append(element)
                oxygen = temp
                k += 1
            else:
                break
        l = 0
        for num in co2Search:
            if len(co2) != 1:
                temp = []
                for element in co2:
                    if element[l] == num:
                        temp.append(element)
                co2 = temp
                l += 1
            else:
                break

    print(oxygen)
    print(co2)
    print(int(oxygen[0], 2) * int(oxygen[0], 2))
        


    
print()