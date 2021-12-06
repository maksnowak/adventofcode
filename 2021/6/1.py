data = open('2021/6/input.txt', 'r').read().strip()
_fish = data.split(',')
fish = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
n = len(_fish)
for timer in _fish:
    fish[timer] += 1
for _ in range(80):
    temp = fish['0']
    fish['0'] = fish['1']
    fish['1'] = fish['2']
    fish['2'] = fish['3']
    fish['3'] = fish['4']
    fish['4'] = fish['5']
    fish['5'] = fish['6']
    fish['6'] = fish['7']
    fish['7'] = fish['8']
    fish['6'] += temp
    fish['8'] = temp

    n += temp
print(n)