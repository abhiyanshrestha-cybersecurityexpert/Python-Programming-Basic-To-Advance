# Calculator 
# Enter a number
# Enter Second Numbe
# Enter operation
# Output shows
# Ask do you want to continue 
# Done by Abhiyan Shrestha

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      if num2 == 0:
        print("Error: Division by zero")
        continue
      else:
        result = num1 / num2
    else:
      print("Invalid operator")
      continue

    print("Result:", result)

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
      break
