size = int(input("Enter the amount of numbers: "))
nums = []
for i in range(size):
    temp = int(input("Enter a number: "))
    nums.append(temp)

negnums = []

for num in nums:
    if num < 0:
        negnums.append(num)

for num in negnums:
    print(num)
