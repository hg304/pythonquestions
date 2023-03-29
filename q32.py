nums = []
for i in range(10):
    nums.append(int(input("Enter a number: ")))

avg = 0
maxi = nums[0]
mini = nums[0]

for i in range(len(nums)):
    avg += nums[i]
    if nums[i] > maxi:
        maxi = nums[i]
    if nums[i] < mini:
        mini = nums[i]

avg = float(avg / len(nums))

print(f"Average: {str(avg)}\nMaximum: {str(maxi)}\nMinimum: {str(mini)}")