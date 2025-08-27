students = {}


def add():
    key = str(input("Please enter the students full name:"))
    while True:
        value = str(input("Please enter the information of the student:"))
        students.update({key: value})
        print("The student has added")
        c = str(input("Do you want to add another information(yes/no):").lower())
        if c == "yes":
            continue
        else:
            break


def remove():
    while True:
        name = str(input("Enter the the name of the student you want to remove:"))
        if name in students:
            del students[name]
        print("The student has removed")
        n = str(input("Do you want to remove another(yes/no)").lower())
        if n == "yes":
            continue
        else:
            break


def student():
    name = str(input("Enter the name of the student you want to find:"))
    if name in students:
        print(students[name])
    else:
        print("This student doesnt exit on the system!")


def view():
    for key, value in student():
        print(f"{key}:{value}")


print("Welcome to student system")
while True:
    ask = int(input((
        "Enter the number of the thing you need:\n1.Add a student \n2.Remove a student\n3.view the "
        "student \n4.find a student\n5.End the program\n")))
    if ask == 1:
        while True:
            add()
            ask = str(input("Do you want to add any other student(yes/no):").lower())
            if ask == "yes":
                continue
            else:
                break
    elif ask == 2:
        while True:
            remove()
            a = str(input("Do you want to remove another student(yes/no):").lower())
            if a == "yes":
                continue
            else:
                break
    elif ask == 3:
        view()
    elif ask == 4:
        student()
    else:
        break
