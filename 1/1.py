with open('1/input.txt', 'r') as f:
    noOfIncreased = 0
    for line in f:
        try:
            if int(line.strip()) > int(prev):
                noOfIncreased += 1
        except:
            noOfIncreased = 0
        prev = line.strip()
    print(noOfIncreased)