n = int(input("Enter a number: "))

if n < 0:
    print("Sequence: 0")

print("Sequence: ", end="")
if n % 2 == 0:
    for i in range(n, -1, -2):
        print(i, end=" ")
else:
    n -= 1
    for i in range(n, -1, -2):
        print(i, end=" ")