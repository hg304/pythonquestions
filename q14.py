import math

vi = int(input("Enter initial velocity: "))
t = 0

h = vi * t - 5 * math.pow(t, 2)

while h >= 0:
    print(f"{str(t)} {str(h)}")
    t += 1
    h = vi * t - 5 * math.pow(t, 2)