size = int(input("Enter the amount of numbers: "))
nums = []
for i in range(size):
    temp = int(input("Enter a number: "))
    nums.append(temp)

maxdiff = 0
for i in range(len(nums)-1):
    if abs(nums[i]-nums[i+1]) > maxdiff:
        maxdiff = abs(nums[i] - nums[i+1])

print(maxdiff)