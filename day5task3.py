#Task 3
# Ask User for the number
# ask for anothe number
# ask user for the operation between those users (+,-,*,/)
# Product output as asked in task
# Done By Abhiyan Shrestha

def calculate():
  
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operation (+, -, *, /): ")

  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    result = num1 / num2

  print("Result:", result)

calculate()