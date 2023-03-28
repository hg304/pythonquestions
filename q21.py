numofnums = int(input("Enter the amount of numbers: "))
nums = []
for i in range(numofnums):
    num = input("Enter a number: ")
    nums.append(num)

for i in range(len(nums)):
    if i == len(nums) - 1:
        print(str(nums[i]), end=".\n")
    else:
        print(str(nums[i]), end=", ")
