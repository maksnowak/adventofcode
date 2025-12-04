from itertools import batched


def first_part(input):
    invalids = []
    with open(input, "r") as f:
        for r in f.readline().split(","):
            min, max = r.split("-")
            min_val = int(min)
            max_val = int(max)
            for i in range(min_val, max_val + 1):
                s = str(i)
                if len(s) % 2 == 0 and s[: len(s) // 2] == s[len(s) // 2 :]:
                    invalids.append(i)
    return sum(invalids)


def second_part(input):
    invalids = []
    with open(input, "r") as f:
        for r in f.readline().split(","):
            min, max = r.split("-")
            min_val = int(min)
            max_val = int(max)
            for i in range(min_val, max_val + 1):
                s = str(i)
                for j in range(1, len(s)):
                    chunks = [batch for batch in batched(s, j)]
                    if chunks.count(chunks[0]) == len(chunks) and i not in invalids:
                        invalids.append(i)

    return sum(invalids)


print(first_part("example.txt"))
print(first_part("input.txt"))
print()
print(second_part("example.txt"))
print(second_part("input.txt"))
