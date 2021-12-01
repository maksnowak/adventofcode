valid = 0
with open("input.txt", "r") as inp:
    for line in inp:
        chars = 0
        i = 1
        (req, passwd) = line.split(": ")
        reqs = req.split(" ")
        nums = reqs[0].split("-")
        for char in passwd:
            if (i == int(nums[0]) or i == int(nums[1])) and char == reqs[1]:
                chars += 1
            i += 1
        if chars == 1:
            valid += 1
print(valid)