#Weekly 1 = Give values
#Weekly 2 = Math Operations
#Weekly 3 = if/elif
#Weekly 4 = random. - while/if/else/break
#Weekly 5 = for - list references
#Weekly 6 = Letter - Tables
#Weekly 7 = try - except
#Weekly 8 = binary - highest/lowest - multiple defs
#Weekly 9 = txt - terminal reading files
def main():
    print("Hello World")
    vone = int(input("Enter a value: "))
    vtwo = int(input("Enter another one: "))

    add = vone + vtwo
    subtract = vone - vtwo
    multiply = vone * vtwo

    ans = input("What math operation would you like to realize?(add)(subtract)(multiply): ").lower()
    attempts = 100
    while attempts > 0:

        if ans == "add":
            print("Your result is: " , add)

        elif ans == "subtract":
            print("Your result is: " , subtract)

        elif ans == "multiply":
            print("Your result is: " , multiply)

            break

        else:
            print("No valid answer, please try again")



if __name__ == "__main__":
    main()
