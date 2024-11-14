# Ask User for the number
# ask for anothe number
# ask user for the operation between those users (+,-,*,/)
# Product output as asked in task
# Done By Abhiyan Shrestha

def calculate():

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    operator = input("Enter a operator(+,-,*,/): ")
    
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == '*':
        result = num1 * num2
    
    elif operator == "/":
        if num2 == 0:
            print("Error: Divison by zero")
            return
        else:
            result = num1 / num2

    else:
        print("Invalid Operation")
        return
    
    print("Result: ", result)
    return

calculate()