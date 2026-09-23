def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    number = int(input("Enter a number (1-10) (stop): "))
    while True:
        print(number * 1)
        print(number * 2)
        print(number * 3)
        print(number * 4)
        print(number * 5)
        print(number * 6)
        print(number * 7)
        print(number * 8)
        print(number * 9)
        print(number * 10)
        if number > 10:
            print("Try again: ")
        elif number < 1:
            print("Try again: ")
        break


if __name__ == "__main__":
    main()

