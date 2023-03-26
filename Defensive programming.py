import os.path

# Define a function to get user input for two numbers and an operator
def get_input():
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Please enter your second number: "))
        op = input("Enter the operation you would like (+, -, /, *): ")
    except ValueError:
        print("Invalid Input")
        exit()

    # Check for valid operator
    if op not in ["+", "-", "/", "*"]:
        print("Invalid Operator")
        exit()

    return num1, num2, op


# Define a function to read equations from a file and print out the equations and their results
def read_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                equation = line.strip()
                try:
                    # Evaluate the equation
                    result = eval(equation)
                    print(f"{equation} = {result}")
                except (NameError, SyntaxError, ZeroDivisionError):
                    print(f"Invalid equation: {equation}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


# Get user input
option = input("Enter '1' to enter two numbers and an operator, or '2' to read equations from a file: ")

if option == "1":
    num1, num2, op = get_input()

    # Perform the calculation based on user input
    try:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "/":
            result = num1 / num2
        elif op == "*":
            result = num1 * num2
        else:
            print("Invalid Operation")
            exit()
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        exit()

    # Display and save the result
    print("Result:", result)

    result_str = str(result) + "\n"  # convert result to string and add a new line

    try:
        with open("calculation.txt", "a") as file:
            file.write(result_str)
    except OSError:
        print("Error saving result to file")

elif option == "2":
    filename = input("Enter the name of the file: ")

    # Check if the file exists
    while not os.path.isfile(filename):
        filename = input(f"File '{filename}' not found. Please enter a valid file name: ")

    # Read equations from file and print out the equations and their results
    read_file(filename)

else:
    print("Invalid option")
