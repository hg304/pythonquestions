nums = []
flag = True
for i in range(10):
    nums.append(int(input("Enter a number: ")))

occurring = {}
big = 0

for i in range(len(nums)):
    if 0 < nums[i] < 99:
        if nums[i] in occurring:
            occurring[nums[i]] += 1
        else:
            occurring[nums[i]] = 1
    else:
        big = nums[i]
        flag = False
        break

bignum = 0
if flag is False:
    print(f"Invalid input: {str(big)} is not in 0-99")
else:
    for num in occurring:
        if occurring[num] > big:
            bignum = num
            big = occurring[num]
    print(f"{str(bignum)} {str(big)}")