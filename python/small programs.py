# 1

def _1():
    x=int(input("nom1 :"))
    y=int(input("nom2 :"))
    z=x
    x=y
    y=z
    print(x,y)


# 2

def _2():
    x=int(input("Enter the nom :"))
    if x%2==1:
        print("This number is odd")
    else:
        print("This number is even")


# 3

def _3():
    s=str(input("Enter the lyrics :"))
    x=list(s)
    x.reverse()
    for i in x:
        print(i,end="")


 
# 4

def _4():
    numbers=[1,2,3,4,5,6,7]
    st=[]
    for i in numbers:
        st.append(str(i))
    print(st)
_4()


# 5

def _5():
    def convert(celsius):
        return celsius*9/5+32
    c=float(input("Enter the temperature in celsius :"))
    f=convert(c)
    print(f" temperature in celsius is {c} and temperature in fahrenheit is {f}")

    
# 6?

def _6():
    x=int(input("Enter the input :"))
    if x.isdigit() :
        print("This input is digit")
    elif x.isdigit():
        print("This input is digit")


# 7

def _7():
    x=str(input("enter the lyrics :"))
    r=""
    for i in x[::-1]:
        r+=i
    if r==x:
        print("this is lyrics is palindrome")
    else :
        print("This syntax isn't palindrome")


# 8

def _8():
    s=str(input("Enter the lyrics :"))
    for s in s[::-1]:
        print(s,end="")


# 9

def _9():
    x="hi"
    y="ahmed"
    x=set(x)
    y=set(y)
    z=x.union(y)
    print(z)
    

# 11

def _11():
    x=int(input("Enter the number :"))
    if x==0:
        print("This number is zero")
    elif x>0:
        print("print this number is positive")
    else:
        print("print this number is negative")


# 12

def _12():
    n1=int(input("Enter the nom1:"))
    n2=int(input("Enter the n2:"))
    n3=int(input("Enter the n3:"))
    print(max(n1,n2,n3))


# 13


# 14 

def _14():
    x=float(input("Enter you degree :"))
    if x<60:
        print("you got F")
    elif x>60 and x<70:
        print("you got c")
    elif x>=70 and x<80:
        print("you got B")
    elif x>=80 and x<90:
        print("you got A")
    elif x>=90:
        print("You got A+")


# 15

def _15():
    x=str(input("Enter the letter :").lower())
    if x=="a" or x=="o" or x=="e" or x=="i" or x=="r":
        print("This is a vowel letter ")
    elif not(x=="a" or x=="o" or x=="e" or x=="i" or x=="r"):
        print("This letter isn't a vowel letter")


# 16

def _16():
    x=int(input("Enter the hour :"))
    if x<=6:
        print("Good night!")
    elif x>6 and x<=12:
        print("Good morning")
    elif x>12 and x<=18:
        print("Good afternoon|!")
    elif x>18 and x<24:
        print("Good ")


# 17

def _17():
    l1=float(input("Enter the first side length :"))
    l2=float(input("Enter the second side length :"))
    l3=float(input("Enter the third side length :"))
    if(l1==l2==l3):
        print("This triangle is equilateral triangle")
    elif (l1==l2) or(l2==l3) or (l3==l1):
        print("This triangle is iscoiles !")
    elif not((l1==l2) or(l2==l3) or (l3==l1)):
        print("This triangle is scalen ")


# 18



# 19

def _19():
    i=int(input("Enter the number :"))
    if i>0 and i<50:
        print("The number is between (0,50)")
    elif i>50 and i<=100 :
        print("This nom is between (49,100) ")
    elif i>100 and i<150:
        print("This number is between (100,150)")
    else:
        print("This number is above 150")


# 20

def _20():
    x=int(input("Enter the number :"))
    sum=0
    for i in range (3):
        sum+=x
        x+=1
    print(sum)


# 21


# 22

def _22():
    x=float(input("Enter the number :"))
    x=str(x)
    x=list(x)
    print(len(x))


# 23

def _23():
    noms=[]
    while True:
        x=int(input("Enter the number you want to add"))
        noms+=x
        a=str(input("Do you want to add any other thing(yes/no):").lower())
        if a=="yes":
            continue
        elif a=="no":
            print(noms)
            break


# 24

def _24():
    noms=[0,1]
    for i in range (5):
        n=noms[-1]+noms[-2]
        noms.append(n)
    print(noms)


# 25

def _25():
    n=int(input("Enter a nom:"))  
    counter=2 
    s=0
    while counter<=n:
        s+=counter
        counter+=2
    print(s)

