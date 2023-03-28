time = input("Enter the time in this format: hh mm am/pm ")

time = time.split(" ")
hours = time[0]
minutes = time[1]
setting = time[2]

newtime = ""


if setting == "am":
    if int(hours) == 12:
        newtime += "00"
    elif 0 < int(hours) < 10:
        newtime += "0" + hours
    elif int(hours) == 10 or int(hours) == 11:
        newtime += hours
    else:
        print("Invalid input")
else:
    if int(hours) == 12:
        newtime += "12"
    elif 0 < int(hours) < 12:
        newtime += str(12 + int(hours))
    else:
        print("Invalid input")

newtime += ':' + minutes

print(newtime)

