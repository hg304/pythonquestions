dat = input("Enter the date: ")
dat = dat.split(" ")
day = int(dat[0])
month = int(dat[1])
year = int(dat[2])

if day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
    day = 1
    month += 1
    print(f"{str(day)} {str(month)} {str(year)}")
elif day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    if month == 12:
        day = 1
        month = 1
        year += 1
    else:
        day = 1
        month += 1
    print(f"{str(day)} {str(month)} {str(year)}")
elif day == 28 and month == 2:
    day = 1
    month += 1
    print(f"{str(day)} {str(month)} {str(year)}")
else:
    print("Incorrect input")

