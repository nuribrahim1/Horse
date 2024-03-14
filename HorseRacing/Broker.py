from Horse import *
from random import randint


print("Hello welcome to Super Stables")
nameList = ["a","b","c","d","e","f","g"]

def newbet():

    h1 = horse(random.choice(nameList),randint(11,18),130,(255,0,0))
    h2 = horse(nameList[randint(0,6)],randint(11,18),150,(10,10,10))
    h3 = horse(nameList[randint(0,6)],randint(11,18),170,(0,0,255))
    h4 = horse(nameList[randint(0,6)],randint(11,18),190,(255,165,0))
    h5 = horse(nameList[randint(0,6)],randint(11,18),210,(238,130,238))

    print (f"The horses racing today are\n"
           f"1) {h1.name} Odds: {h1.odds}\n"
           f"2) {h2.name} Odds: {h2.odds}\n"
           f"3) {h3.name} Odds: {h3.odds}\n"
           f"4) {h4.name} Odds: {h4.odds}\n"
           f"5) {h5.name} Odds: {h5.odds}")

    bet = " "
    while bet.upper() != "Y" and bet.upper() != "N":
        bet = input("Would you like to bet on a horse (Y/N)\n")
        if  bet.upper() == "Y":
            r1 = race(h1,h2,h3,h4,h5)
            pass
        elif bet.upper() == "N":
            print ("Come back tomorrow")
            return (newbet())
        else:
            print("Incorrect input")

    amount = 0
    paying = True
    while paying:
        amount = input("How much money would you like to bet\n£")
        if amount.isnumeric():
            if int(amount) > 0:
                amount = int(amount)
                paying = False
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    choice  = 0
    chosing = True
    while chosing:
        choice  = input("Which horse would like to bet on (1-5)")
        if choice == "1":
            steed = r1.h1
            chosing = False
        elif choice == "2":
            steed = r1.h2
            chosing = False
        elif  choice == "3":
            steed = r1.h3
            chosing = False
        elif choice == "4":
            steed = r1.h4
            chosing = False
        elif choice == "5":
            steed = r1.h5
            chosing = False
        else:
            print("Invalid input")

    print(f"You have chosen {steed.name}")

    r1.begin()
    if steed != r1.winner:
        print(f"Sorry, you have lost £{amount}")
    else:
        print(f"Congratulations, you have won £{amount*(20-steed.speed)}")

newbet()
