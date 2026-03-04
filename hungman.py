import random

# Word list
words = ["python", "computer", "hangman", "programming", "developer"]

# Pick random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")

while wrong_guesses < max_wrong:
    display_word = ""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")
    
    if all(letter in guessed_letters for letter in word):
        print("\n You Win! The word was:", word)
        break
else:
    print("\n You Lost! The word was:", word)