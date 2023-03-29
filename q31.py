throws = []
scores = []

for i in range(21):
    temp = int(input("Enter the throw value: "))
    throws.append(temp)

f = 0
t = 0
for f in range(9):
    score = throws[t]
    if score == 10:
        score += throws[t+1] + throws[t+2]
    else:
        t += 1
        score += throws[t]
        if score == 10:
            score += throws[t+1]
    t += 1

    if f > 0:
        score += scores[f-1]
    scores.append(score)

scores[f] = scores[f - 1] + throws[t] + throws[t+1] + throws[t+2]

f = 0
for f in range(10):
    print(scores[f], end=" ")
