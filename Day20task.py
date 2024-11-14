# Requirement
# Ask user to login or register
# if register ask the user for username, password,usertype and write their user data in a file
# if login ask the user for username and password and check on the userdata stored file
# if login successful: give seller user two choices: 1. add product and buyer only 2. view product
# Add product : ask the user for product name, description and price and write the data in file
# view Product: print the data from the text file that is there
# ask buyer which product do you want to purchase
# find if the product exist or not and if not found print invalid name 
# but if it exist ask for quantity and create a  bill data (productname,buyername,quanity,total price)
# put option view bills of the buyer
# Buyer bill must be only print as user
# and store it in a file
# Done by Abhiyan Shrestha

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    usertype = input("Enter usertype (seller/buyer): ")

    with open("userdatas.txt", "a") as f:
        f.write(f"{username},{password},{usertype}\n")
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    with open("userdatas.txt", "r") as f:
        for line in f:
            user, pwd, usertype = line.strip().split(",")
            if username == user and password == pwd:
                return usertype
    print("Invalid username or password")
    return None

def add_product():
    product_name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))

    with open("products.txt", "a") as f:
        f.write(f"{product_name},{description},{price}\n")
    print("Product added successfully!")

def view_products():
    try:
        with open("products.txt", "r") as f:
            print("Product Name\tDescription\tPrice")
            for line in f:
                try:
                    name, desc, price = line.strip().split(",")
                    print(f"{name}\t\t{desc}\t\t{price}")
                except ValueError:
                    print("Error: Invalid data format in products.txt")
    except FileNotFoundError:
        print("Error: products.txt file not found")

def purchase_product():
    view_products()
    product_name = input("Enter product name to purchase: ")

    product_found = False
    with open("products.txt", "r") as f:
        for line in f:
            try:
                name, desc, price = line.strip().split(",")
            except ValueError:
                print(f"Error: Invalid data format in products.txt: {line}")
                continue  # Skip to the next line

            if name == product_name:
                product_found = True
                quantity = int(input("Enter quantity: "))
                total_price = float(price) * quantity
                buyer_name = input("Enter your name: ")

                with open("bills.txt", "a") as f:
                    f.write(f"{product_name},{buyer_name},{quantity},{total_price}\n")
                print("Purchase successful!")
                break
        if not product_found:
            print("Invalid product name")


def view_bills():
    buyer_name = input("Enter your name: ")
    with open("bills.txt", "r") as f:
        print("Product Name\tBuyer Name\tQuantity\tTotal Price")
        for line in f:
            product, buyer, quantity, price = line.strip().split(",")
            if buyer == buyer_name:
                print(f"{product}\t\t{buyer}\t\t{quantity}\t\t{price}")

def main():
    while True:
        choice = input("1. Register\n2. Login\nq. Quit\n")
        if choice == "1":
            register()
        elif choice == "2":
            usertype = login()
            if usertype:
                if usertype == "seller":
                    while True:
                        choice = input("1. Add product\n2. View products\nq. Logout\n")
                        if choice == "1":
                            add_product()
                        elif choice == "2":
                            view_products()
                        elif choice == "q":
                            break
                        else:
                            print("Invalid choice")
                else:
                    while True:
                        choice = input("1. View products\n2. Purchase product\n3. View bills\nq. Logout\n")
                        if choice == "1":
                            view_products()
                        elif choice == "2":
                            purchase_product()
                        elif choice == "3":
                            view_bills()
                        elif choice == "q":
                            break
                        else:
                            print("Invalid choice")
        elif choice == "q":
            break
        else:
            print("Invalid choice")

main()