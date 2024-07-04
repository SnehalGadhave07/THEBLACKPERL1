
import sys
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number!"
    else:
        return x ** 0.5

def power(x, y):
    return x ** y

def display_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")
    return choice
def main():
    while True:
        choice = display_menu()
        
        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '6':
                print("Result:", power(num1, num2))
        elif choice == '5':
            try:
                num = float(input("Enter the  number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue
            
            print("Result:", square_root(num))
        else:
            print("Invalid choice! Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
