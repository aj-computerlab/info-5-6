def main():
    def highest(a,b):

        if a > b:
            print(f"The highest number is {a}")

        else:
            print(f"The highest number is {b}")

    value1 = int(input("Enter a number: "))
    value2 = int(input("Enter a number: "))
    highest (value1,value2)

    def lowest(a,b,c):

            if a > b:
                print(f"The highest number is {a}")

            else:
                print(f"The highest number is {b}")

        value1 = int(input("Enter a number: "))
        value2 = int(input("Enter a number: "))
        highest (value1,value2)

if __name__ == "__main__":
    main()
