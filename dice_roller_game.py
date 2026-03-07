import random


print("welcome to dice battle: ")

name=input("Enter your name : ").capitalize()

print(f"let's begin {name}")

start=input("yes/no: ").lower()

while start== "yes":
    comp_roll=random.randint(1,6) 
      
    your_roll=random.randint(1,6)

    if comp_roll>your_roll:
        print(f"computer won! computer dice: {comp_roll}, your dice: {your_roll}")
    elif comp_roll==your_roll:
        print("its a tie")
    else:
        print(f"you won!!computer dice: {comp_roll}, your dice: {your_roll}")

    start=input("start again ? (yes /no)").lower()
print("thanks for playing!!",name)