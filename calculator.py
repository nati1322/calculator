def read_number(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt))
            return number
        except:
            print("please enter a correct number")
            continue


if __name__ == "__main__":
    while True:
        num1 = read_number("enter the 1st number: ?")
        operator = input("Enter an operator (+ - * /): ")
        num2 = read_number("Enter the 2nd number: ")

        if operator == "+":
            result = num1 + num2
            print(round(result, 3))
        elif operator == "-":
            result = num1 - num2
            print(round(result, 3))
        elif operator == "*":
            result = num1 * num2
            print(round(result, 3))
        elif operator == "/":
            result = num1 / num2
            print(round(result, 3))
        else:
            print(f"{operator} is not a valid operator")
        x = input("would you like to continue yes,no: ?")
        if x != "yes":
            print("good bye")
            break
