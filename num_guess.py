import random
#random used to get random numbers

num=random.randint(1,100)
attempts=10
print("NUMBER GUESSING GAME FROM 1-100")
print(f"you have {attempts} to guess")
print("LET'S BEGIN!!")
while attempts>0:
    guess_num=int(input("enter the number you guessed: "))
    if num == guess_num:
        print("wow you guessed it right")
        break
    elif num>guess_num:
        print("TOO LOW LOL!!! GUESS HIGHER!!!")
    else:
        print("TOO HIGH LOL!!! GUESS LOWER!!")
    attempts-=1
    print("attempts left: ",attempts)
if attempts==0:
    print("LOL!! cant even guess!! GAME OVER ")
