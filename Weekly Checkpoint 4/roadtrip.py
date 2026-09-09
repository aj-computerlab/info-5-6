def main():
    answer = "" #1. initialize
    followup = ""
    
    while answer != "Yes!": #2. Condition
        answer = input("Are we there yet? ").strip().title() #3. Update
        if answer == "Yes":
            followup = input("Really? ").strip().title()
        if followup == "Yes!":
            break

    print("We just arrived!")

if __name__ == "__main__":
    main()
