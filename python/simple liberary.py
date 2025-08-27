books=["head","body","python"]
def buy():
    b=str(input("Enter the name of book you want to buy:"   ))
    if b in books:
        books.remove(b)
    else:
        print("we donot have this book")

def sell():
    s=str(input("enter the name of the book you want to sell:"))
    c = int(input("enter the coast of this book"))
    if c>=300:
        print("sorry too exipensive")
    elif c<=300:
        print("ok,the book is selled")
        books.append(s)
print("hello to my simple liberary projram")

while True:
    ask=str(input("do you want to (buy/sell/view the books) a book"))
    if ask=="buy":
        while True:
            print("the books we have for now is {}".format(books))
            buy()
            i=str(input("do you want to buy any thing else?"))
            if i=="yes":
                continue
            elif i=="no":
                break
    elif ask=="sell":
        while True:
            sell()
            s=str(input("do you want to sell any thing else?"))
            if s=="yes":
                continue
            else:
                break
    elif ask=="view the books":
        print(books)
