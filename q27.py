max = 0
nums = []

size = int(input("Enter the amount of numbers: "))
nums = []
for i in range(size):
    temp = int(input("Enter a number: "))
    nums.append(temp)

for num in nums:
    if num > max:
        max = num

print(max)