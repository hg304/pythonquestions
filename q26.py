size = int(input("Enter the amount of numbers: "))
nums = []
for i in range(size):
    temp = int(input("Enter a number: "))
    nums.append(temp)

flag = True
i = 0
while flag is True and i < len(nums)-1:
    if nums[i] > nums[i+1]:
        flag = False
    i += 1

if flag is True:
    print("Sorted")
else:
    print("Unsorted")