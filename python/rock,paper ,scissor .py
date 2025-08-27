import random
choises=("paper","scissors","rock")
print("hello to my rock,paper ,scissor game")
score={'robot':0,'you':0}
while True:
    a=str(input("please enter your guss"))
    b=random.choice(choises)
    if a=="rock":
        if b=="paper":
            print("the robot choose","=",b)
            print("you lose")
            score['robot']+=1
        elif b=="rock":
            print("the robot choose","=",b)
            print("draw")
        elif b=="scissors":
            print("the robot choose","=",b)
            print("you win")
            score['you']+=1
        elif a=="paper":
            print("the robot choose","=",b)
            print("draw")
    elif a=="scissor":
        if b=="paper":
            print("the robot choose","=",b)
            print("you win")
            score['you']+=1
        elif b=="rock":
            print("the robot choose","=",b)
            print("you lose")
            score['robot']+=1
        elif b=="scissors":
            print("draw")
    elif a=="paper":
        if b=="paper":
            print("the robot choose","=",b)
            print("draw")
        elif b=="rock":
            print("the robot choose","=",b)
            print("you win")
            score['you']+=1
        elif b=="scissors":
            print("the robot choose","=",b)
            print("you lose")
            score['robot']+=1
    print(score)
    x=str(input("do you want to play again?"))
    if x=="yes":
        continue
    else:
        break


