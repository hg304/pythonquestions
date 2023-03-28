plate = input("Enter license plate: ")
plate = list(plate)

carry = False

if plate[5] < '9':
    plate[5] = chr(ord(plate[5]) + 1)
    carry = False
else:
    plate[5] = '0'
    carry = True

if carry == True:
    if plate[4] < '9':
        plate[4] = chr(ord(plate[4]) + 1)
        carry = False
    else:
        plate[4] = '0'
        carry = True

if carry == True:
    if plate[3] < '9':
        plate[3] = chr(ord(plate[3]) + 1)
        carry = False
    else:
        plate[3] = '0'
        carry = True

if carry == True:
    if plate[2] < 'Z':
        plate[2] = chr(ord(plate[2]) + 1)
        carry = False
    else:
        plate[2] = 'A'
        carry = True

if carry == True:
    if plate[1] < 'Z':
        plate[1] = chr(ord(plate[1]) + 1)
        carry = False
    else:
        plate[1] = 'A'
        carry = True

if carry == True:
    if plate[0] < 'Z':
        plate[0] = chr(ord(plate[0]) + 1)
        carry = False
    else:
        plate[0] = 'A'
        carry = True

newplate = ""
for c in plate:
    newplate += c

print(newplate)