t_l = {}


def add():
    name = str(input("Enter the task :"))
    t_l.update({name: "uncompleted"})
    print("The task has added!")


def remove():
    name = str(input("Enter the name of the task you want to delete :"))
    if name in t_l:
        del t_l[name]
        print("The task has removed")
    else:
        print("This task dont exist !")


def mark():
    name = str(input("Please enter the name of task you want to mark as complete:"))
    if name in t_l:
        t_l.update({name: "completed"})
        print("The task is completed!")
    else:
        print("This task doesnt exist !")
def view():
    for key,value in t_l.items():
        print(f"{key}:{value}")


print("Hello to 'to do list' program!")
while True:
    d = int(
        input("Please enter the number of the process you need\n1.Add a new task\n2.Remove a task\n3.Mark a task as "
              "completed\n4.View the tasks\n"))
    if d == 1:
        while True:
            add()
            ask = str(input("Do you want to add other task (yes/no):"))
            if ask == "yes":
                continue
            elif ask == "no":
                print("___________________________________")
                break
            else:
                print("Wrong input!")
                break
    elif d == 2:
        while True:
            remove()
            ask=str(input("Do you want to remove another task(yes/no):"))
            if ask == "yes":
                continue
            elif ask == "no":
                print("___________________________________")
                break
            else:
                print("Wrong input!")
                break
    elif d == 3:
        mark()
        print("___________________________________")
    elif d == 4:
        view()
        print("___________________________________")
    else:
        print("You only can enter(1/2/3/4)")
        continue

