_sum = 0
with open("input.txt", "r") as f:
    for group in f.read().split("\n\n"):
        answers = []
        for person in group.split("\n"):
            for question in person:
                answers.append(question)
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        for letter in alphabet:
            num = answers.count(letter)
            if num == len(group.split()):
                _sum += 1
print(_sum)