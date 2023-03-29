passes  = []
num = int(input("Enter a number: "))

temp = input("Enter: ")
passes = temp.split(" ")
longest = 0
tempcount = 0

for pas in passes:
    if pas != "I":
        tempcount += 1
    else:
        if tempcount != 0:
            if tempcount > longest:
                longest = tempcount