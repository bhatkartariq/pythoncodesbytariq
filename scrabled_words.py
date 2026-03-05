import random

words = ["python", "computer", "science", "developer", "keyboard"]

word = random.choice(words)
letters = list(word)
random.shuffle(letters)

scrambled = "".join(letters)

attempts = 3

print(" Word Scramble Game ")
print("Unscramble:", scrambled)

while attempts > 0:
    guess = input("Your guess: ")

    if guess == word:
        print(" Correct! YOU WON!!!")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print(" Game Over! The word was:", word)