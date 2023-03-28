import math

x = input("Enter x1 and y1: ")
xs = x.split(" ")
x1 = float(xs[0]); y1 = float(xs[1])

y = input("Enter x2 and y2: ")
ys = y.split(" ")
x2 = float(ys[0]); y2 = float(ys[1])

d = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

print(d)