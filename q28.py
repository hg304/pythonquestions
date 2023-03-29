values = []

for i in range(12):
    temp = int(input("Enter a number: "))
    values.append(temp)

for i in range(0, len(values), 4):
    print(f"{str(values[i])} {str(values[i+1])} {str(values[i+2])} {str(values[i+3])}")