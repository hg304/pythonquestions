chapters  = []

for i in range(15):
    temp = int(input("Enter 1 if you wish to get the chapter, 0 if you don't: "))
    chapters.append(temp)

pick = ""
threshold = 0
i = 0
pos = 0
for i in range(len(chapters)):
    start = i + 1
    if pos != 0 and i <= pos:
        continue

    if chapters[i] == 1 and i < len(chapters)-3:
        end = 0
        for j in range(i, len(chapters)):
            if chapters[j] == 1:
                threshold += 1
            if chapters[j] == 0 or j == len(chapters):
                if threshold >= 3:
                    end = j
                    break
                else:
                    break
        if end != 0:
            pick += f"{str(start)}-{str(end)} "
            pos = end
            i = end + 1
            end = 0
            threshold = 0
        else:
            pick += f"{str(start)} "
            threshold = 0
    else:
        if chapters[i] == 1:
            pick += f"{str(start)} "

print(pick)

