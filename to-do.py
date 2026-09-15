def main():
    tasks = []
    while True:
        print(f"You have {len(tasks)} tasks to do.")
        print(tasks)
        command = input("What do you want to do? (add, complete, or stop): ").lower()
        if command == "add":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
        elif command == "complete":
            outtask = input("Which task are you removing?: ")
            tasks.remove(outtask)
        elif command == "stop":
            break


if __name__ == "__main__":
    main()
