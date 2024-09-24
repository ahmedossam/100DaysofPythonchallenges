# List of operators
operators = ["+", "-", "*", "/"]

# Function to perform basic arithmetic
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:  # Check to avoid division by zero
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input(f"Enter an operator from {operators}: ")

# Perform the calculation
result = calculate(num1, num2, operator)
print(f"The result is: {result}")
