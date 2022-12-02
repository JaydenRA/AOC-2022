games = open("data.txt", "r").read().splitlines()

def Q1():
    score = 0
    for game in games:
        if game[2] == "X":
            score += 1
            if game[0] == "A":
                score += 3
            elif game[0] == "C":
                score += 6
        elif game[2] == "Y":
            score += 2
            if game[0] == "B":
                score += 3
            elif game[0] == "A":
                score += 6
        else:
            score += 3
            if game[0] == "C":
                score += 3
            elif game[0] == "B":
                score += 6
    return score

def Q2():
    score = 0
    for game in games:
        if game[2] == "Y":
            if game[0] == "A":
                score += 4
            elif game[0] == "B":
                score += 5
            else:
                score += 6
        elif game[2] == "X":
            if game[0] == "A":
                score += 3
            elif game[0] == "B":
                score += 1
            else:
                score += 2
        else:
            if game[0] == "A":
                score += 8
            elif game[0] == "B":
                score += 9
            else:
                score += 7
    return score
            
print(f"Q1: {Q1()}\nQ2: {Q2()}")
