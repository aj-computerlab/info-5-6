import random

def main():
    coin = ["heads", "tails"] #square brackets for lists
    flip = random.choice(coin)
    guess = input("Heads or tails?: ").strip().lower()

    print("The coin landed on", flip)

    if guess == flip:
        print("You won!")
    else:
        print("You lost")

if __name__ == "__main__":
    main()
