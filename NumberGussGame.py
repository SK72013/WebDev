print ("Welcome to Number Guessing Game")
print("Rule: User must guess the number which chose by the computer. Let's Begin")
print("Computer's Number:x ")

import random
c_number = random.randint(1,10)

chance = 5

while True :

    print(f"You have {chance} Chance left !")
     
    u_number = int(input("Guess the number (1-10) : "))
    chance = chance -1

    if chance == 0 :
        print("You are lost the game. Better luck next time !")
        break
     
     
    if  u_number == c_number :
        print("Congratulation ! You Won")
        break
    if u_number != c_number:
        if u_number > c_number:
            print("Try lower numbers.")
        elif u_number < c_number:
            print("Try higher numbers.")
        continue


    
 
