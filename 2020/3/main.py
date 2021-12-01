def slope(right, even):
    i = 0
    line_num = 1
    trees = 0
    with open("input.txt", "r") as f:
        for line in f:
            check = list(line)
            if even:
                if line_num % 2 == 1:
                    if check[i] == "#":
                        trees += 1
                    i += right
                    if i >= 31:
                        i -= 31
                line_num += 1
            else:
                if check[i] == "#":
                    trees += 1
                i += right
                if i >= 31:
                    i -= 31
    return trees
print(slope(1, False) * slope(3, False) * slope(5, False) * slope(7, False) * slope(1, True))