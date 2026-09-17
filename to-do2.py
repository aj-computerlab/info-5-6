def main():

    tasks = []

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)

        new_task = input("Enter task: ").capitalize().strip()

        if new_task == "Exit":
            break

        elif new_task not in tasks:
            tasks.append(new_task)
        elif new_task in tasks:
            del_confirm = input(f"Did you completed {new_task}? (y/n): ").lower().strip()
            if del_confrim == "y":
                tasks.remove(new_task)
            else:
                continue

if __name__ == "__main__":
    main()
