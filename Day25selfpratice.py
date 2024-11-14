# Requirement
# Create a calculator that calculates +,-,/,* using while loop and def function
# Done by Abhiyan Shrestha


while True:
    num1 = float(input('Enter 1st Number: '))
    num2 = float(input('Enter 2nd Number: '))
    operations = input('+,-,*,/: ')
                
    if operations == '+':
        results = num1 + num2
            
    elif operations == '-':
        results = num1 - num2

    elif operations == '*':
        results = num1 * num2

    elif operations == '/':
        if num2 == 0:
            print("Error: Division by zero")
            continue
        else:
            results = num1 / num2
    else:
        print("Invalid operator")
        continue

    print('Results:',results)