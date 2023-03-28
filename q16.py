n = int(input("Enter a number: "))

while n > 0:
    sum = 0
    for i in range(n):
        m = int(input("Enter a number: "))
        sum += m
    print(f"Sum: {str(sum)}")
    n = int(input("Enter a number:"))