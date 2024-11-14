# task 1 - store any data in variable and result =  10 times
# single line
# Done By Abhiyan Shrestha

a = '20' # Storing a as 20 in variable as data

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20

print(a) # output will be printed 20
#############################################################################################

#Task 2
# Ask User for the number
# ask for anothe number
# ask user for the operation between those users (+,-,*,/)
# Product output as asked in task
# Done By Abhiyan Shrestha

def calculate():
    num1 = float(input("Enter Num1: "))
    num2 = float(input("Enter Num2: "))
    operator = input("Enter operator(+,-,*,/): ")

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
#########################################################################################

# Task 3 (Exam Result)
# Ask the user for his or her exam total percentage
# if the percenge is between 90 to 100 print outstanding
# if the percentage is between 80 to 90 print excellent
# if the percentage is between 70 to 80 print very good
# if the percentage is between 60 to 70 print good
# if the percentage is between 50 to 60 print Better
# if the percentage is between 40 to 50 print passed
# if the percentage is below 40 print fail
# Done By Abhiyan Shrestha

totalpercentage = float(input("Enter Percentage here: "))

if totalpercentage >= 90 and totalpercentage <= 100:
    print("Outstanding")

elif totalpercentage >= 80 and totalpercentage <= 90:
    print("Excellent")

elif totalpercentage >= 70 and totalpercentage <= 80:
    print("Very Good")

elif totalpercentage >= 60 and totalpercentage <= 70:
    print("Good")

elif totalpercentage >= 50 and totalpercentage <= 60:
    print("Better")

elif totalpercentage >= 40 and totalpercentage <= 50:
    print("Passed")    

elif totalpercentage <40:
    print("Fail")

else:
    print("100 percent is max that can be typed thank you!")
######################################################################################

# task 4
# Ask the user for a word which he/she wants to print
# Ask the user for how many times does he/she wants to print
# Print the word for as many times as the user told
# Done by Abhiyan Shrestha

word = input("Enter any word: ")
times = float(input("How many times: "))
count = 0

while count < times:
    print(word)
    count += 1

###########################################################################################