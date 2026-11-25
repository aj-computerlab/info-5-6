def main():
    vone = float(input("Enter value 1: "))
    vtwo = float(input("Enter value 2: "))
    op = input("Enter arithmetic operator sign: ")
    sum = vone + vtwo
    sub = vone - vtwo
    mul = vone * vtwo
    div = vone / vtwo

    if op == "+":
        print("Your result is: ", sum)
    elif op == "-":
        print("Your result is: ", sub)
    elif op == "*":
        print("Your result is: ", mul)
    elif op == "/":
        print("Your result is: ", div)


if __name__ == "__main__":
    main()
