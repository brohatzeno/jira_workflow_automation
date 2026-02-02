#!/usr/bin/env python3
"""
Simple CLI Calculator
Supports basic arithmetic operations: addition, subtraction, multiplication, division
"""

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

def main():
    """Main calculator function"""
    print("Simple CLI Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        # Take input from the user
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # Error message
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()