valid = 0
with open("input.txt", "r") as f:
    for passport in f.read().split("\n\n"):
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        d = {}
        info = passport.split()
        for data in info:
            (key, val) = data.split(":")
            d[key] = val
        if "byr" in d:
            if 1920 <= int(d["byr"]) <= 2002:
                byr = True
        if "iyr" in d:
            if 2010 <= int(d["iyr"]) <= 2020:
                iyr = True
        if "eyr" in d:
            if 2020 <= int(d["eyr"]) <= 2030:
                eyr = True
        if "hgt" in d:
            height = list(d["hgt"])
            if height[-1] == "n" and height[-2] == "i":
                if 59 <= int(height[0] + height[1]) <= 76:
                    hgt = True
            elif height[-1] == "m" and height[-2] == "c":
                if len(height) == 5:
                    if 150 <= int(height[0] + height[1] + height[2]) <= 193:
                        hgt = True
        if "hcl" in d:
            char = list(d["hcl"])
            acceptable = set('0123456789abcdef')
            def isAcceptable(s):
                return set(s) <= acceptable
            if char[0] == "#" and isAcceptable(char[1] + char[2] + char[3] + char[4] + char[5] + char[6]):
                hcl = True
        if "ecl" in d:
            if d["ecl"] == "amb" or d["ecl"] == "blu" or d["ecl"] == "brn" or d["ecl"] == "gry" or d["ecl"] == "grn" or d["ecl"] == "hzl" or d["ecl"] == "oth":
                ecl = True
        if "pid" in d:
            if len(d["pid"]) == 9:
                pid = True
        if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
            valid += 1
print(valid)