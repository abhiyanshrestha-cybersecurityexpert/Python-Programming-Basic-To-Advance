# Requirement
# if he/she is buyer or seller
# if the user is seller ask him/her product name, description, price,  and write this product data in file
# Done by Abhiyan Shrestha

def seller():
    user_role = input("Are you a buyer or seller? (buyer/seller): ")

    if user_role == "seller":
        product_name = input("Enter product name: ")
        product_description = input("Enter product description: ")
        product_price = input("Enter product price: ")

        with open("ecommerce.txt", "a") as file:
            file.write(f"Product Name: {product_name}\n")
            file.write(f"Description: {product_description}\n")
            file.write(f"Price: {product_price}\n\n")
        print("Product data saved successfully!")

if __name__ == "__main__":
    seller()


