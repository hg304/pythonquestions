bina = input("Enter a 8 bit binary number separated by spaces: ")
bina = bina.split(" ")
sum = 0
count = 1

for i in range(len(bina)-1, -1, -1):
    if bina[i] == '1':
        sum = sum + count
    if count == 1:
        count += 1
    else:
        count *= 2

print(sum)
