def quist():
    score=0
    print("1. What is the largest animal on the planet?")
    print("A. Elephant")
    print("B. Giraffe")
    print("C. Blue Whale")
    print("D. Alligator")
    answer=str(input("A,b,c or d").lower())
    if answer=="c":
        print("correct")
        score+=1
        print("your score is {}".format(score))
    else:
        print(" false")
    print("___________________")
    print("\n2. Which planet is known as the Red Planet?")
    print("A. Earth")
    print("B. Mars")
    print("C. Jupiter")
    print("D. Venus")
    answer=str(input("A,b,c or d").lower())
    if answer=="b":
        print("you win")
        score+=1
        print("your score is {}".format(score))
    else:
        print("false")
    print("___________________")
    print("\n5. What is the smallest prime number?")
    print("A. 0")
    print("B. 1")
    print("C. 2")
    print("D. 3")
    answer=str(input("A,b,c or d").lower())
    if answer=="a":
        print("you win")
        score+=1
        print("your score is {}".format(score))
    else:
        print("false")
        print("your score is {}".format(score))
print("hello to the quiz ?")

quist()
    

