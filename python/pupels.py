studnets = {}


def add():
    name = str(input("Please enter the name of studnet:"))
    g = int(input("Please enter the grade of the studnet:"))
    studnets.update({name: g})
    print("The studnet has added to the system!")


def remove():
    name = str(input("Please enter the name of the studnet:"))
    if name in studnets:
        del studnets[name]
        print("The studnet has removed!")
    elif name not in studnets:
        print("This name doesnt exist on the system!")
    else:
        print("Something went wrong! you may entered wrong input")


def change():
    name = (str(input("Please enter the name of student you want to change his degree:")))
    if name in studnets:
        d = int(input("Please enter the new degree :"))
        studnets.update({name: d})
    elif name not in studnets:
        print("Sorry this name doesnt exist in the system!")
    else:
        print("You may entered wrong input")


def view():
    for x, y in studnets.items():
        print(f"{x}:{y}")


print("Hello to pupels grades system!")
while True:
    d = int(input(
        "Please enter the number of process you want\n1.Add a new pupil\n2.Remove a previews pupil\n3.Change a degree "
        "of student\n4.view the pupels\n"))
    if d == 1:
        while True:
            add()
            ask = str(input("Do you want to add another studnet to the system (yes/no):").lower())
            if ask == "yes":
                print("_______________________________________")
                continue
            else:
                break
                print("_______________________________________")
            print("_______________________________________")
    elif d == 2:
        while True:
            remove()
            ask = str(input("Do you want to remove another student (yes/no):").lower())
            if ask == "yes":
                print("_______________________________________")
                continue
            else:
                break
                print("_______________________________________")
            print("_______________________________________")
    elif d == 3:
        change()
        print("_______________________________________")
    elif d == 4:
        print("_______________________________________")
        view()
        print("_______________________________________")
    else:
        print("Sorry but you may enter a wrong input you can only enter (1/2/3/4)")
