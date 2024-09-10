
from fractions import Fraction
import math
import sys
from datetime import datetime

# Define arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def exponentiate(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(x)

# Convert input to Fraction if it contains '/'
def parse_input(value):
    try:
        # Check if input is a fraction
        if '/' in value:
            return Fraction(value)
        # Otherwise, treat it as a float
        return float(value)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number or fraction.")

# Print menu options
def print_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Square Root")
    print("7. View History")
    print("8. View Statistics")
    print("9. Exit")

# Print calculation history
def print_history(history):
    if not history:
        print("No history available.")
    else:
        print("\nCalculation History:")
        for entry in history:
            print(entry)
        print()

# Print statistics of calculations
def print_statistics(history):
    if not history:
        print("No history available.")
        return

    results = [entry.split('=')[1].strip() for entry in history if '=' in entry]
    
    try:
        results = [float(result) for result in results]
    except ValueError:
        print("Error: Unable to parse history results.")
        return

    total = sum(results)
    average = total / len(results)

    print(f"\nTotal of last results: {total}")
    print(f"Average of last results: {average:.2f}\n")

# Save history to a file
def save_history(history):
    with open('history.txt', 'a') as file:
        for entry in history:
            file.write(f"{datetime.now()}: {entry}\n")

# Load history from a file
def load_history():
    try:
        with open('history.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

# Main function
def main():
    history = load_history()

    while True:
        print_menu()
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '9':
            print("Exiting...")
            save_history(history)
            sys.exit()

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                if choice in ['5', '6']:
                    num1 = parse_input(input("Enter number: "))
                    if choice == '5':
                        num2 = parse_input(input("Enter exponent: "))
                        result = exponentiate(num1, num2)
                        operation = f"{num1} ^ {num2} = {result}"
                    elif choice == '6':
                        result = sqrt(float(num1))
                        operation = f"sqrt({num1}) = {result}"
                else:
                    num1 = parse_input(input("Enter first number: "))
                    num2 = parse_input(input("Enter second number: "))
                    
                    if choice == '1':
                        result = add(num1, num2)
                        operation = f"{num1} + {num2} = {result}"
                    elif choice == '2':
                        result = subtract(num1, num2)
                        operation = f"{num1} - {num2} = {result}"
                    elif choice == '3':
                        result = multiply(num1, num2)
                        operation = f"{num1} * {num2} = {result}"
                    elif choice == '4':
                        result = divide(num1, num2)
                        operation = f"{num1} / {num2} = {result}"

                print(operation)
                history.append(operation)
                save_history(history)
            
            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        elif choice == '7':
            print_history(history)
        
        elif choice == '8':
            print_statistics(history)
        
        else:
            print("Invalid choice. Please select a valid option.")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
