with open('data.txt') as f:
    lines = f.readlines()

highest = 0
temp = 0

top2 = 0
top3 = 0

for line in lines:
    if line != "\n":
        temp += int(line)
    else:
        if temp > highest:
            top2 = highest
            highest = temp
        elif temp > top2:
            top3 = top2
            top2 = temp
        elif temp > top3:
            top3 = temp
        temp = 0

print(f"Q1: {highest}\nQ2: {highest+top2+top3} ")
