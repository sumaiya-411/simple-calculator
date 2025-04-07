# Simple Calculator Program

# Define basic math operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

# Main calculator function
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation from the list below:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Oops! That’s not a valid option.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers only.")
        return

    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '×'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '÷'

    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
