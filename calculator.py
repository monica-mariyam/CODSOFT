'''A simple calculator with basic arithmetic operations.
Prompt user to input two numbers and an operation choice.
Perform the calculation and display the result.'''
import sys

#function that performs addition operation
def add(num1,num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

#function that performs subtraction operation
def subtract(num1,num2):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

#function that performs multiplication operation
def multiply(num1,num2):
    result = num1 * num2
    print(f"{num1} X {num2} = {result}")

#function that performs division operation
def divide(num1,num2):
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")

#function that performs modulo division operation
def modulo(num1,num2):
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")

#function that performs integer division operation
def integer(num1,num2):
    result = num1 // num2
    print(f"{num1} // {num2} = {result}")

#function that performs power operation
def power(num1,num2):
    result = pow(num1,num2)
    print(f"{num1} ^ {num2} = {result}")


   
print('-'*120)
print(' '*50,'SIMPLE CALCULATOR',' '*50)
print('-'*120)
while True:
    try:
        print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.MODULO DIVISION\n6.INTEGER DIVISION\n7.POWER")
        print('-'*120)
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        choice = int(input("Enter your operation choice number : "))
        if choice == 1:
            add(num1,num2)
        elif choice == 2:
            subtract(num1,num2)
        elif choice == 3:
            multiply(num1,num2)
        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError("Alert : Denominator should not be zero. Please enter any integer other than zero.")
            divide(num1,num2)
        elif choice == 5:
            if num2 == 0:
                raise ZeroDivisionError("Alert : Denominator should not be zero. Please enter any integer other than zero.")
            modulo(num1,num2)
        elif choice == 6:
            if num2 == 0:
                raise ZeroDivisionError("Alert : Denominator should not be zero. Please enter any integer other than zero.")
            integer(num1,num2)
        elif choice == 7:
            power(num1,num2)
        else:
            print("Invalid choice. Please enter a valid choice.")


        print("-"*120)
        ch = input("Do you want to try more operations(yes/no)? ")
        print("-"*120)
        if ch.lower() == 'no':
            sys.exit()

    except ValueError as e:
        print("Alert : Please enter a valid integer!!!")
        print("-"*120)

    except ZeroDivisionError as e:
        print(e)
        print("-"*120)

    
