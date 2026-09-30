def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if 1 <= number <= 10:


                print("Number stored succesfully.")
                not_validated = False # --> break
        except ValueError:
            print("Enter a NUMBER!😡")

if __name__ == "__main__":
    main()
