set={}
def add():
    while True:
        des=str(input("enter the description you want to add"))
        value=int(input("enter the value of the cost of the object"))
        set.update({des:value})
        ask =str(input("do you want to add any thing else?"))
        if ask=="yes":
            continue
        else:
            break
def remove():
    remove=str(input("enter the description "))
    if remove in set:
        del set[remove]
        print("the object has removed")
    else:
        print("this task donot exist ")
def calculate():
    total=sum(set.values())
    print("the total of expinsis if {} dollars".format(total))
print("hello to expinces system")
while True:
    f=str(input("do you want to (add / remove/ calculat/ view the list)"))
    if f=="add":
        add()    
    elif f=="remove":
        while True:
            remove()
            d=str(input("do you want to remove any other thing"))
            if d=="yes":
                continue
            else:
                break
    elif f=="calculate":
        calculate()
    elif f=="view the list":
        print(set)
    else:
        d=str(input("do you want to do any thing else"))
        if d=="yes":
            continue
        else:
            break



   

