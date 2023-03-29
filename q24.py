import math
diagonal = float(input("Enter a diagonal value: "))

for i in range(1, int(diagonal)):
    h = math.sqrt((diagonal**2) - (i**2))
    if i > h:
        print(f"Height: {str(h)}   Width: {str(i)}")