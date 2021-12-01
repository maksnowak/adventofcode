inp = input().split()
broken = False
for a in inp:
    for b in inp:
        for c in inp:
            if int(a) + int(b) + int(c) == 2020:
                broken = True
                break
        if broken:
            break
    if broken:
        break
print(int(a), int(b), int(c), int(a) * int(b) * int(c))
