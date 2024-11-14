# Requirement
# Ask user for login or register
# if register : ask for username and password  and write data in file
# if login: ask the username and password userdata is in the file or not if it in the file login successfull or ivailid credencial
# Done by Abhiyan Shrestha
import json # this is a module

user_choice = input('Do you want to login or register: ')

if user_choice == 'register':
    user_name = input('Enter username: ')
    user_password = input('Enter Password: ')

    user_dict_data = {user_name:user_password}
    user_json_data = json.dumps(user_dict_data)

    f = open('userdata.txt','a')
    f.write(str(user_dict_data))
    print('Login Successfull')
    f.close() 