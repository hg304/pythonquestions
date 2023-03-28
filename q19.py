password = input("Enter a password: ")
lengthcheck = False
lettercheck = False
numbercheck = False
charactercheck = False

if len(password) >= 8:
    lengthcheck = True

for char in password:
    if char == '!' or char == '#' or char == '%':
        charactercheck = True
    if char.isalpha():
        lettercheck = True
    if char.isdigit():
        numbercheck = True

if lengthcheck == False:
    print("Too short")

if lettercheck == False:
    print("Missing letter")

if numbercheck == False:
    print("Missing number")

if charactercheck == False:
    print("Missing special")

if lengthcheck == lettercheck == numbercheck == charactercheck == True:
    print("OK")
