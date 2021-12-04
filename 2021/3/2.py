def check(rating):
    with open('2021/3/input.txt', 'r') as f:
        data = f.read().splitlines()
        for i in range(12):
            noOfZero = 0
            noOfOne = 0
            if len(data) != 1:
                temp = []
                for num in data:
                    if num[i] == "0":
                        noOfZero += 1
                    else:
                        noOfOne += 1
                if rating == "oxygen":
                    if noOfOne >= noOfZero:
                        for num in data:
                            if num[i] == "1":
                                temp.append(num)
                        data = temp
                    else:
                        for num in data:
                            if num[i] == "0":
                                temp.append(num)
                        data = temp
                elif rating == "co2":
                    if noOfZero <= noOfOne:
                        for num in data:
                            if num[i] == "0":
                                temp.append(num)
                        data = temp
                    else:
                        for num in data:
                            if num[i] == "1":
                                temp.append(num)
                        data = temp
    return data

oxygen = check("oxygen")
co2 = check("co2")

print(int(oxygen[0], 2) * int(co2[0], 2))
