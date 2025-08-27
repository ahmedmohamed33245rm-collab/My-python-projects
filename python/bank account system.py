accounts={}
def add():
    id=int(input("Enter the id number of the new account :"))
    if id in accounts:
        print("This id is already exist!")
    elif id not in accounts:
        name=str(input("Enter the name of the acount :"))
        balance=float(input("Enter the amount of money you want to put in your acount :"))
        accounts[id]={"Name":name,"balance":balance}
        print("The account has added !")

def wd():
    id =int(input("Enter the id number of the account :"))
    if id in accounts:
        a=float(input("Enter the amount you want to take :"))
        accounts[id]["balance"]-=a
        print("The money has taken from the account!")
    elif id not in accounts:
        print("Print there is no account in the system with this id !")

def deposit():
    id=int(input("Enter the id number of the account :"))
    a=float(input("Enter the amount of money you want to deposit :"))
    if id in accounts:
        accounts[id]["balance"]+=a
        print("The money has deposited!")
    else:
        print("This id account doesnot exist in the system!")

def va():
    id =int(input("Enter the id number of the account"))
    if id in accounts:
        print(accounts[id])
    elif id not in accounts:
        print("This id number doesnot exist in the system!")
    
def vas():
    for x,y in accounts.items():
        print(f"{x}:{y}")

print("Hello to the bank system!")
while True:
    d=int(input("Do you want (enter the number of process you need )\n1.Add a new account\n2.withdraw a money\n3.Deposit a money\n"
                "4.view a account\n5.view all accounts\n6.End program\n"))
    if d==1:
            add()
    elif d==2:
        wd()
    elif d==3:
        deposit()
    elif d==4:
        va()
    elif d==5:
        vas()
    elif d==6:
        break
    else :
        print("Sorry but you can only enter (1/2/3/4/5/6)")


            