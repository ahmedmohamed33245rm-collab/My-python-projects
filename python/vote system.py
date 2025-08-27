candidates = {}
def add():
    a=str(input("enter the name of candidates you want to add:"))
    candidates.update({a:0})
    print("the candidates has added")
def vote():
    a=str(input("please enter the name of candidates you want to vote:"))
    if a in candidates:
        candidates[a]+=1
    else:
        print("this candidates doesn't exist")
while True:
    ask = int(input("1.add a candidates\n2.vote\n3.view the candidates\n4.end\n="))
    if ask == 1:
        while True:
            add()
            a = str(input("do you want to add any one else:"))
            if a == "yes":
                continue
            else:
                break
    elif ask == 2:
        while True:
            vote()
            s = str(input("do you want to vote to another one:"))
            if s == "yes":
                continue
            else:
                break
    elif ask == 3:
        print(candidates)
        print("________________________")
    else:
        breakpoint()