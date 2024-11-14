# Task-9
# make an dictinary with user data's(username and password)
# ask the user for his or her user name and password
# if the username and password is in dictinary print login successful
# Else Invalid Credentials
# Done by Abhiyan Shrestha

userdata = {'Abhiyan_Shrestha':'Abhiyan123'} # Dictionary key and value is available
username = input('Enter username: ')
password = input("Enter Password: ")

if username in userdata and password == userdata.get(username): # username and password are same or not cheching
    print('Login Successfull!')

else:
    print("Invalid Credentials!") # if username or password is wrong out is invalid credentials