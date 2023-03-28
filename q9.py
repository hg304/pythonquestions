runwayNum = int(input("Enter a number: "))
runwayDeg = runwayNum * 10
direction = ""

if 0 - 22.5 < runwayDeg < 0 + 22.5:
    direction = "north"
elif 45 - 22.5 < runwayDeg < 45 + 22.5:
    direction = "northeast"
elif 90 - 22.5 < runwayDeg < 90 + 22.5:
    direction = "east"
elif 135 - 22.5 < runwayDeg < 135 + 22.5:
    direction = "southeast"
elif 180 - 22.5 < runwayDeg < 180 + 22.5:
    direction = "south"
elif 225 - 22.5 < runwayDeg < 225 + 22.5:
    direction = "southwest"
elif 270 - 22.5 < runwayDeg < 270 + 22.5:
    direction = "west"
elif 315 - 22.5 < runwayDeg < 315 + 22.5:
    direction = "northwest"

print(f"{str(runwayDeg)} degrees ({direction})")
