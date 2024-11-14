# Requirement
# Ask user to login or register
# if register ask the user for username, password, and write their user data in a file
# if login ask the user for username and password and check on the userdata stored file
# if login successful: give user two choices: 1. add product 2. view product
# Add product : ask the user for product name, description and price and write the data in file
# view Product: print the data from the text file that is there    
# Done by Abhiyan Shrestha

def register():
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    with open('userdatas.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    print('Thank You for registering!')

def login():
    username = input('Username: ')
    password = input('Password: ')

    user_found = False
    with open('userdatas.txt', 'r') as file:
        for line in file:
            user, password_hash = line.strip().split(',')
            if username == user and password == password_hash:
                user_found = True
                break

    if user_found:
        print('Login successful!')
        user_choice = input('Choose an option:\n1. Add product\n2. View products\n')
        if user_choice == '1':
            add_product()
        elif user_choice == '2':
            view_products()
        else:
            print('Invalid choice')
    else:
        print('Invalid username or password')

def add_product():
    product_name = input('Enter product name: ')
    description = input('Enter product description: ')
    price = input('Enter product price: ')

    with open('products.txt', 'a') as file:
        file.write(f"Name: {product_name},Description: {description},Price: {price}\n")
    print('Product added successfully!')

def view_products():
    print('Products:')
    with open('products.txt', 'r') as file:
        for line in file:
            product_name, description, price = line.strip().split(',')
            print(f"Name: {product_name}, Description: {description}, Price: {price}")

user_choice = input('Do you want to login or register: ')

if user_choice == 'register':
    register()
elif user_choice == 'login':
    login()
else:
    print('Invalid choice')