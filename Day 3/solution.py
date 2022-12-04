f = open("data.txt", "r").read().split()

#1
q1 = 0

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for inv in f:
    left = inv[: int(len(inv) / 2)]
    right = inv[int(len(inv) / 2) :]

    char = [char_ for char_ in right if char_ in left][0]

    q1 += (1 + priorities.rfind(char))

print(q1)

#2
q2 = 0

groups = zip(*(iter(f),) * 3)

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for group in groups:
    char = list(set.intersection(*map(set, group)))[0]
    q2 += (1 + priorities.rfind(char))

print(q2)
