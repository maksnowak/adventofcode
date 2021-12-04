data = open('2021/4/input.txt', 'r').read().split()
nums = data[0].split(',')
_boards = data[1:]
winning = 0
_sum = 0
boards = [[] for _ in range(100)]
won = []
i = 0
for num in _boards:
    boards[i].append(num)
    if len(boards[i]) == 25:
        i += 1
for num in nums:
    for i, board in enumerate(boards):
        if num in board:
            board[board.index(num)] = "*"
        for j in range(0, 20, 5):
            if board[j] == board[j + 1] == board[j + 2] == board[j + 3] == board[j + 4]:
                if len(won) < 98 and boards[i] not in won:
                    won.append(boards[i])
                elif boards[i] in won:
                    pass
                else:
                    winning = i
                    break
        for k in range(0, 5):
            if board[k] == board[k + 5] == board[k + 10] == board[k + 15] == board[k + 20]:
                if len(won) < 98 and boards[i] not in won:
                    won.append(boards[i])
                elif boards[i] in won:
                    pass
                else:
                    winning = i
                    break
        if winning != 0:
            break
    if winning != 0:
        last = int(num)
        break
for num in boards[winning]:
    try:
        _sum += int(num)
    except:
        pass
print(_sum * last)