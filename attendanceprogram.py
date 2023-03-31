import csv
import openpyxl

global f
f = openpyxl.load_workbook(filename="attendance.xlsx")

def listOfTraineesManip(sheet):
    while True:
        print("OPTIONS:\n1. Add trainee\n2. Delete trainee\n3. Update trainee\n4. Exit")
        choice = int(input("Pick a choice: "))
        if choice == 1:
            id = int(input("Enter the trainee's id: "))
            firstName = input("Enter the trainee's first name: ")
            lastName = input("Enter the trainee's last name: ")
            course = input("Enter the course the trainee is taking: ")
            background = input("Enter the trainee's background (degree/work experience): ")
            lastRow = 0
            for cellObj in sheet.rows:
                lastRow += 1
            sheet.insert_rows(lastRow+1)
            row = [id, firstName, lastName, course, background]
            for i in range(len(row)):
                sheet.cell(row=lastRow+1, column=i+1).value = row[i]
            f.save(filename="attendance.xlsx")

        elif choice == 2:
            toDelete = False
            row = 0
            id = int(input("Enter the existing trainee's id: "))
            for cellObj in sheet.rows:
                row += 1
                if cellObj[0].value == id:
                    toDelete = True

            if toDelete == False:
                print("Trainee with given ID could not be found")
            else:
                sheet.delete_rows(idx=row)
                f.save(filename="attendance.xlsx")

        elif choice == 3:
            toEdit = False
            row = 0
            id = int(input("Enter the existing trainee's id: "))
            for cellObj in sheet.rows:
                row += 1
                if cellObj[0].value == id:
                    toEdit = True

            if toEdit == False:
                print("Trainee with given ID could not be found")
            else:
                firstName = input("Enter the trainee's first name: ")
                lastName = input("Enter the trainee's last name: ")
                course = input("Enter the course the trainee is taking: ")
                background = input("Enter the trainee's background (degree/work experience): ")
                for cellObj in sheet.rows:
                    if cellObj[0].value == id:
                        cellObj[1].value = firstName
                        cellObj[2].value = lastName
                        cellObj[3].value = course
                        cellObj[4].value = background
                        break
                f.save(filename="attendance.xlsx")

        elif choice == 4:
            break
        else:
            print("Incorrect choice")

def listOfTrainersManip(sheet):
    while True:
        print("OPTIONS:\n1. Add trainer\n2. Delete trainer\n3. Update trainer\n4. Exit")
        choice = int(input("Pick a choice: "))
        if choice == 1:
            id = int(input("Enter the trainer's id: "))
            firstName = input("Enter the trainer's first name: ")
            lastName = input("Enter the trainer's last name: ")
            email = input("Enter the trainer's email: ")
            phone = int(input("Enter the trainer's phone number: "))
            lastRow = 0
            for cellObj in sheet.rows:
                lastRow += 1
            sheet.insert_rows(lastRow+1)
            row = [id, firstName, lastName, email, phone]
            for i in range(len(row)):
                sheet.cell(row=lastRow+1, column=i+1).value = row[i]
            f.save(filename="attendance.xlsx")

        elif choice == 2:
            toDelete = False
            row = 0
            id = int(input("Enter the existing trainer's id: "))
            for cellObj in sheet.rows:
                row += 1
                if cellObj[0].value == id:
                    toDelete = True

            if toDelete == False:
                print("Trainer with given ID could not be found")
            else:
                sheet.delete_rows(idx=row)
                f.save(filename="attendance.xlsx")

        elif choice == 3:
            toEdit = False
            row = 0
            id = int(input("Enter the existing trainer's id: "))
            for cellObj in sheet.rows:
                row += 1
                if cellObj[0].value == id:
                    toEdit = True

            if toEdit == False:
                print("Trainer with given ID could not be found")
            else:
                firstName = input("Enter the trainer's first name: ")
                lastName = input("Enter the trainer's last name: ")
                email = input("Enter the trainer's email: ")
                phone = int(input("Enter the trainer's phone number: "))
                for cellObj in sheet.rows:
                    if cellObj[0].value == id:
                        cellObj[1].value = firstName
                        cellObj[2].value = lastName
                        cellObj[3].value = email
                        cellObj[4].value = phone
                        break
                f.save(filename="attendance.xlsx")

        elif choice == 4:
            break
        else:
            print("Incorrect choice")

def courseDetailsManip(sheet):
    while True:
        print("OPTIONS:\n1. Add Course\n2. Delete Course\n3. Update course\n4. Exit")
        choice = int(input("Pick a choice: "))
        if choice == 1:
            id = input("Enter the course's id: ")
            description = input("Enter what the course is: ")
            lastRow = 0
            for cellObj in sheet.rows:
                lastRow += 1
            sheet.insert_rows(lastRow+1)
            row = [id, description]
            for i in range(len(row)):
                sheet.cell(row=lastRow+1, column=i+1).value = row[i]
            f.save(filename="attendance.xlsx")

        elif choice == 2:
            toDelete = False
            row = 0
            id = input("Enter the existing course's id: ")
            for cellObj in sheet.rows:
                row += 1
                if cellObj[0].value == id:
                    toDelete = True

            if toDelete == False:
                print("Course with given ID could not be found")
            else:
                sheet.delete_rows(idx=row)
                f.save(filename="attendance.xlsx")

        elif choice == 3:
            toEdit = False
            row = 0
            id = int(input("Enter the existing trainee's id: "))
            for cellObj in sheet.rows:
                row += 1
                if cellObj[0].value == id:
                    toEdit = True

            if toEdit == False:
                print("Course with given ID could not be found")
            else:
                description = input("Enter what the course is: ")
                for cellObj in sheet.rows:
                    if cellObj[0].value == id:
                        cellObj[1].value = description
                        break
                f.save(filename="attendance.xlsx")

        elif choice == 4:
            break
        else:
            print("Incorrect choice")

def mapCourseTrainee(map, course, trainee):
    while True:
        print("OPTIONS:\n1. Map course and trainees\n2. Exit")
        choice = int(input("Pick a choice: "))
        if choice == 1:
            row = 0
            for courseObj in course.rows:
                row += 1
                rowlist = []
                for traineeObj in trainee.rows:
                    if courseObj[0].value == traineeObj[2].value:
                        rowlist.append(traineeObj[0].value)
                map.insert_rows(row)
                map.cell(row=row, column=1).value = courseObj[0].value
                for i in range(len(rowlist)):
                    if map.cell(row=row, column=2).value == None:
                        map.cell(row=row, column=2).value = str(rowlist[i])
                    else:
                        map.cell(row=row, column=2).value += ", " + str(rowlist[i])
            f.save(filename="attendance.xlsx")
        elif choice == 2:
            break


def accessSheet(sheet):
    if sheet.title == "ListOfTrainees":
        listOfTraineesManip(sheet)

def openSheet(sheetname):
    return f[sheetname]

def menu():
    i = 1
    sheet = None
    while True:
        for name in f.sheetnames:
            print(f"{i}. {str(f[name])}")
            i += 1
        choice = int(input("Choose the sheet you wish to edit: "))
        if choice == 1:
            sheet = openSheet("ListOfTrainees")
            listOfTraineesManip(sheet)
        elif choice == 2:
            sheet = openSheet("ListOfTrainers")
            listOfTrainersManip(sheet)
        elif choice == 3:
            sheet = openSheet("CourseDetails")
            courseDetailsManip(sheet)
        elif choice == 4:
            sheet1 = openSheet("MappingCourseTrainees")
            sheet2 = openSheet("CourseDetails")
            sheet3 = openSheet("ListOfTrainees")
            mapCourseTrainee(sheet1, sheet2, sheet3)
        elif choice == 5:
            sheet = openSheet("MappingCourseTrainers")
        elif choice == 6:
            break
        else:
            print("Incorrect choice")

    if sheet != None:
        accessSheet(sheet)

menu()