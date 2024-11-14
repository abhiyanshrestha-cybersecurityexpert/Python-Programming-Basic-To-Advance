##########################################
# Task -2
# Make  a list of usernames
# ask the user for his or her username
# Check that username in the list
# If the user name  is in list print "login successfull"
# Else is the username is not in the list and output will be "Invalid Usernames"
# Done by Abhiyan Shrestha

user_name = ['abhiyan','ram','sita','gopal']
userid = input('Enter User Name:')
ls = 'Login Successful'
iu = 'Invalid Username'

if userid in user_name:
    print(ls)
else:
    print(iu)
