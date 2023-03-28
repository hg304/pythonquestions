inputs = []

temp = 1

while temp != 0:
    temp = int(input("Enter a number: "))
    inputs.append(temp)

total = 0
valid = 0
invalid = 0
for number in inputs:
    if 2 <= number <= 12:
        total += number
        valid += 1
    else:
        if number == 0:
            continue
        invalid += 1

avg = total / valid

print(f"Average: {str(avg)}\nValid: {str(valid)}\nInvalid: {str(invalid)}")