# task (Exam Result)
# Ask the user for his or her exam total percentage
# if the percenge is between 90 to 100 print outstanding
# if the percentage is between 80 to 90 print excellent
# if the percentage is between 70 to 80 print very good
# if the percentage is between 60 to 70 print good
# if the percentage is between 50 to 60 print Better
# if the percentage is between 40 to 50 print passed
# if the percentage is below 40 print fail
# Done By Abhiyan Shrestha

enterhere = float(input("Enter percentage: "))

if enterhere >= 90 and enterhere <= 100:
    print("Outstanding")

elif enterhere >=80 and enterhere <= 90:
    print("Excellent")

elif enterhere >= 70 and enterhere <= 80:
    print("Very Good")

elif enterhere >= 60 and enterhere <= 70:
    print("Good")

elif enterhere >= 50 and enterhere <= 60:
    print("Better")

elif enterhere <= 40:
    print("Fail")

else:
    print("Invalid Input")


