import time
def main():
    name = input("HI! What's your name?: ").title().strip()
    reason = input("What's the reason of your alarm?: ")
    alarm = int(input(f"Hi {name} the reason of you alarm is to {reason}"))
    duration = input("In how much do we remember you?:")

if __name__ == "__main__":
    main()
