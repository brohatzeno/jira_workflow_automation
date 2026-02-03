#!/usr/bin/env python3
#This is a small calculator project
#This is a new commit
#Second attempt

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    """Power function"""
    return x ** y

def modulo(x, y):
    """Modulo function"""
    if y == 0:
        return "Error: Division by zero!"
    return x % y

def display_menu():
    """Display calculator menu options"""
    print("\n" + "="*30)
    print("SIMPLE CLI CALCULATOR")
    print("="*30)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    print("7. Exit")
    print("="*30)

def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None

def main():
    """Main calculator function"""
    print("Welcome to the CLI Calculator!")

    while True:
        display_menu()
        choice = input("\nEnter choice (1-7): ")

        if choice == '7':
            print("\nExiting calculator. Thank you for using our calculator!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1, num2 = get_numbers()

            # Check if input was valid
            if num1 is None or num2 is None:
                continue

            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")

            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")

            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")

            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # Error message
                    print(f"\n{result}")
                else:
                    print(f"\n{num1} / {num2} = {result}")

            elif choice == '5':
                result = power(num1, num2)
                print(f"\n{num1} ^ {num2} = {result}")

            elif choice == '6':
                result = modulo(num1, num2)
                if isinstance(result, str):  # Error message
                    print(f"\n{result}")
                else:
                    print(f"\n{num1} % {num2} = {result}")
        else:
            print("\nInvalid choice! Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
    print("Calculator session ended successfully")