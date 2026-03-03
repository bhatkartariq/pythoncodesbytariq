import random
print("welcome-rock/paper/scissors-game")
choices = ["rock", "paper", "scissors"]
win = 0
compwin = 0

while win < 2 and compwin < 2:
    user = input("Enter rock, paper, or scissors: ").lower()
    comp = random.choice(choices)
    
    print(f"Computer choice: {comp}")

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    if user == comp:
        print(f"It's a tie! Score -> You: {win} | Computer: {compwin}")

    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        win += 1
        print(f"You won this round! Score -> You: {win} | Computer: {compwin}")

    else:
        compwin += 1
        print(f"You lost this round! Score -> You: {win} | Computer: {compwin}")

print("\nFinal Result:")
if win == 2:
    print(" You won the game!")
else:
    print(" Computer won the game!")