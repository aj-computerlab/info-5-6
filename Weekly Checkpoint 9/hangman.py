# Use a import.Random
# Create a TXT file with all of the words.
# Define the main function.
# Present the game "Welcome.. want to start? yes/no      if = yes=print     else = no=print
# Call the start_game function

# Define new function start_game(file).
# Use with to open the TXT file.
# choose = random.choice(Txt)
# print("Enter a Letter to guess the word", choose)
# Create a while loop so the program runs as long the user still has lives

import random

def main():
    start_game("word_bank.txt")

def start_game(file):
    attempts = 10
    with open(file) as f:
        word_bank = f.read().splitlines()
    word = random.choice(word_bank)
    hint = ["_"] * len(word)
    incorrect_letters = []
    while attempts > 0:
        print("Current word:", " ".join(hint))

        while True:
            guess = input ("Guess a letter: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")

        if guess in word and guess not in hint:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts = -1
            print("You already guessed that letter! Attempts left:", str(attempts))

        if "_" not in hint:
            print("Congratulations! 🥳 You guessed the word:", word)
            break

    if attempts == 0 and "_" in hint:
        print("No attempts left 💀 The word was:", word)

if __name__ == "__main__":
    main()

