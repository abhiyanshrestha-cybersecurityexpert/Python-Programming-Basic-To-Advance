# Make  a list of usernames
# ask the user for his or her username
# Check that username in the list
# If the user name  is in list print "login successfull"
# Else is the username is not in the list and output will be "Invalid Usernames"
# Done by Abhiyan Shrestha

user_name = ['Ram', 'Abhiyan', 'Babi']
user_id = input('Enter User Id:')
Successfull = 'Login Successfull'
Invalid = 'Invalid Usernames'

if user_id in user_name:
    print(Successfull)
else:
    print(Invalid)