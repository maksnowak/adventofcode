import re
_sum = 0
with open("input.txt", "r") as f:
    correct = []
    d = {}
    for line in f:
        d[line.strip(".\n").split(" bags contain ")[0]] = line.strip(".\n").split(" bags contain ")[1]
    shiny = re.compile('shiny gold')
    for key, val in d.items():
        if shiny.search(val):
            correct.append(key)
    def search(phrase, val):
        if re.search(phrase, val):
            return 1
        else:
            return 0
    for key, val in d.items():
        for bag in correct:
            _sum += search(bag, val)
print(_sum)
