n = int(input("Enter a number: "))

digit = n % 10

while n > 0:
    print(digit)
    n = n // 10
    digit = n % 10