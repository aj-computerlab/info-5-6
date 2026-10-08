def main():

    print("Welcome to the times table quiz")

    while True:

        try:
            times_table = int(input("Enter a times table to be tested from (1-10): "))
            if times_table >0 and times_table <10:

                break
            else:
                print("enter a number 1 and 10!!!")

        except ValueError:
            print("please put a number")



    while True:
        try:
            max_value = int(input("Enter the max value for your times table: "))
            if max_value > 0:
                break
            else:
                print("put a number greater than 0")
        except ValueError:
            print("put a number")



    max_value += 1

    print(f"\nHere is your quiz for {times_table} times table")

    for x in range(1, max_value):
        correct_answer = x * times_table

        print(f"\n{x} times {times_table} is?")

        while True:
            try:
                user_answer = int(input("your answer: "))
                break
            except ValueError:
                print("you need to put a number")

        if user_answer == correct_answer:
            print("correct")

        else:
            print("incorrect")



if __name__ == "__main__":
    main()
