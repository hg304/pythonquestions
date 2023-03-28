age = int(input("Enter age of passenger: "))
checked = int(input("Enter amount of bags being checked: "))
carryon = int(input("Enter either 0 or 1 carry on is being taken: "))

airfare = 0

if age <= 2:
    airfare = 0
elif age >= 60:
    airfare = 290
else:
    airfare = 300

if carryon == 1:
    airfare += 10
elif carryon > 1:
    print("Invalid amount entered")

if checked == 2:
    airfare += 25
elif checked > 2:
    airfare += 25
    for i in range(1, checked-1):
        airfare += 50

print("Your final fare is " + str(airfare))
