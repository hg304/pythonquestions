import math

n = int(input("Enter a number: "))

if n < 0:
    n = abs(n)

print("Sequence: ", end="")
for i in range(-n, n + 1):
    print(i, end=" ")