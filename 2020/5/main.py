seats = []
with open("input.txt", "r") as f:
    for line in f:
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7
        i = 0
        while i < 7:
            if line[i] == "F":
                i += 1
                max_row -= 2 ** (7 - i)
            elif line[i] == "B":
                i += 1
                min_row += 2 ** (7 - i)
        while i >= 7 and i < 10:
            if line[i] == "L":
                if i == 7:
                    power = 2
                elif i == 8:
                    power = 1
                elif i == 9:
                    power = 0
                max_col -= 2 ** power
                i += 1
            if line[i] == "R":
                if i == 7:
                    power = 2
                elif i == 8:
                    power = 1
                elif i == 9:
                    power = 0
                min_col += 2 ** power
                i += 1
        if min_row == max_row and max_col == min_col:
            seatid = min_row * 8 + max_col
            seats.append(seatid)
        for x in range(min(seats), max(seats)):
            if x not in seats and x+1 in seats and x-1 in seats:
                yours = x
print(yours)