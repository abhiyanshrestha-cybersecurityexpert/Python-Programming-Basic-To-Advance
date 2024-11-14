# Requirements
# Basic Program of python
# Create a program that can do operations like +,-,*,/ using if, elif, else, while
# Done by Abhiyan Shrestha

while True:
    num1 = float(input('Enter Num1: '))
    num2 = float(input('Enter Num2: '))
    operations = input('+,-,*,/: ')

    if operations == '+':
        print(num1 + num2)
    
    elif operations == '-':
        print(num1 - num2)
    
    elif operations == '*':
        print(num1 * num2)
    
    elif operations == '/':
        if num2 == 0:
            print('Error: Cannot be divisible by 0')
        
        else:
            print(num1 / num2)
    else:
        print('Invalid Input')