if __name__ == "__main__":
word = random.choice(word_bank)
def main():
else:
print("Current word:", " ".join(hint))
import random
while attempts > 0:
incorrect_letters = []
if "_" not in hint:
hint = ["_"] * len(word)
print("Great guess!")
if guess not in incorrect_letters:
word_bank = f.read().splitlines()
attempts -= 1
start_game("words.txt")
if guess in word and guess not in hint:
for i in range(len(word)):
print(f"Incorrect letters: {" ".join(incorrect_letters)}")
def start_game(file):
guess = input("Guess a letter: ").lower()
print("Invalid guess. Try again.")
break
attempts = 10
if word[i] == guess:
main()
elif guess in hint:
print("Congratulations! 🥳 You guessed the word:", word)
print("Wrong guess! Attempts left:", str(attempts))
with open(file) as f:
incorrect_letters.append(guess)
if attempts == 0 and "_" in hint:
while True:
print("You already guessed that letter! Attempts left:", str(attempts))
if len(guess) == 1:
print("No attempts left 💀 The word was:", word)
hint[i] = guess
attempts -= 1
else:
break
