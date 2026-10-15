def main():
    #with open("sample.txt") as file:
    #    content = file.read()
    #    print(content)

    #Turn file into a list
    #with open("sample.txt") as hoco_week:
    #    hoco_list = hoco_week.read().splitlines()

    #for day in range(len(hoco_list)):
    #   print(f"Day {day + 1}: {hoco_list[day]}")
    largest("numbers.txt")

def largest(file):
    with open(file) as num_file:
        num_list = num_file.read().splitlines()

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])

    print(max(num_list))

if __name__ == "__main__":
    main()
