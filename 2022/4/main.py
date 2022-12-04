def firstPuzzle(file):
    data = open(file, 'r').read().strip().split('\n')
    fully_contained = 0
    for pair in data:
        jobs = pair.split(',')
        tasks = [job.split('-') for job in jobs]
        if all([int(tasks[0][0]) >= int(tasks[1][0]), int(tasks[0][1]) <= int(tasks[1][1])]) or all([int(tasks [1][0]) >= int(tasks[0][0]), int(tasks[1][1]) <= int(tasks[0][1])]):
            fully_contained += 1
    return fully_contained


def secondPuzzle(file):
    data = open(file, 'r').read().strip().split('\n')
    overlapping = 0
    for pair in data:
        jobs = pair.split(',')
        tasks1 = [i for i in range(int(jobs[0].split('-')[0]), int(jobs[0].split('-')[1]) + 1)]
        tasks2 = [i for i in range(int(jobs[1].split('-')[0]), int(jobs[1].split('-')[1]) + 1)]
        for task in tasks1:
            if task in tasks2:
                overlapping += 1
                break
    return overlapping


print(firstPuzzle('example.txt'))
print(firstPuzzle('input.txt'))

print(secondPuzzle('example.txt'))
print(secondPuzzle('input.txt'))
