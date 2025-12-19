# Simple Calculator in Python

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(f"Addition of two numbers is: {num1 + num2}")
elif operator == "-":
    print(f"Subtraction of two numbers is: {num1 - num2}")
elif operator == "*":
    print(f"Multiplication of two numbers is: {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"Division of two numbers is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator")
