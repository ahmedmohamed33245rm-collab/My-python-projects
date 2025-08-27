import random
def guessgame():
        attemps=0
        r=random.randint(1,10)
        while True:
            h=int(input("please enter your guess"))
            if h==r:
                print("right")
                print("you tried {} times".format(attemps))
                break
            elif h>r:
                print("very high")
                attemps+=1
            elif h<r:
                print("very low ")
                attemps+=1
            
print("hi to number guess game")
guessgame()
while True:
    ask=str(input("do you want to play again"))
    if ask!="yes":
        break
     