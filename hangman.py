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

    start_game("List.txt")

def start_game(file):
    with open(file) as word_file:
        words = word_file.read().splitlines()

    for i in range(len(words)):
        words[i] = int(words[i])

    print(max(words))

if __name__ == "__main__":
    main()
