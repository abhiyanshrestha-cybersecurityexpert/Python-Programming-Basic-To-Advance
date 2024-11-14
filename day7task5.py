# Printing task
# Ask the user for a word which he/she wants to print
# Ask the user for how many times does he/she wants to print
# Print the word for as many times as the user told
# Done by Abhiyan Shrestha

word = input("Enter a word: ")
Times = int(input("How Many times: "))
count = 0

while count < Times:
    print(word)
    count += 1 