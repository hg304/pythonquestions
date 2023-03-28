sentence = input("Enter a sentence")

words = 0
inword = False
for i in range(len(sentence)):
    if sentence[i] == " ":
        inword = False

    elif not inword:
        words += 1
        inword = True


print(words)