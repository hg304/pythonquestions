names = input("Input the names of 3 people in the course: ")

names = names.split(" ")
firstName1 = names[0]; firstName2 = names[2]; firstName3 = names[4]
lastName1 = names[1]; lastName2 = names[3]; lastName3 = names[5]

if firstName1 == "none" and firstName2 == "none" and firstName3 == "none":
    print("TBD")
if firstName1 != "none":
    if firstName2 != "none":
        if firstName3 != "none":
            print(f"{lastName1} / {lastName2} / ...")
        else:
            print(f"{lastName1} / {lastName2}")
    else:
        print(f"{firstName1[0]}. {lastName1}")