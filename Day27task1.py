# Requirement (OOP Concept use)
# Libary Management System
# Give user three choice 1. add book, 2. view all book 3. search book 4. remove book
# 1. add book: ask user for book name, description, price, author make this relational value and store it
# 2. view all book: print all the books
# 3. search book: ask for book name and print the book by searching it
# 4. remove book: ask for book name and delete it.
# Done by Abhiyan Shrestha

class Book:
    def __init__(self, name, description, price, author):
        self.name = name
        self.description = description
        self.price = price
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Enter the book name: ")
        description = input("Enter the book description: ")
        price = int(input("Enter the book price: "))
        author = input("Enter the book author: ")

        book = Book(name, description, price, author)
        self.books.append(book)
        print(f"Book '{name}' added successfully.\n")

    def view_all_books(self):
        if self.books:
            print("All books in the library:")
            for book in self.books:
                print(f"\nName: {book.name}\nDescription: {book.description}\nPrice: {book.price}\nAuthor: {book.author}\n")
        else:
            print("No books in the library.\n")

    def search_book(self):
        name = input("Enter the book name to search: ")
        found = False
        for book in self.books:
            if book.name() == name():
                print(f"\nBook Found:\nName: {book.name}\nDescription: {book.description}\nPrice: {book.price}\nAuthor: {book.author}\n")
                found = True
                break
        if not found:
            print(f"Book '{name}' not found in the library.\n")

    def remove_book(self):
        name = input("Enter the book name to remove: ")
        found = False
        for book in self.books:
            if book.name() == name():
                self.books.remove(book)
                print(f"Book '{name}' removed successfully.\n")
                found = True
                break
        if not found:
            print(f"Book '{name}' not found in the library.\n")

def library_system():
    library = Library()
    
    while True:
        print('1. Add Book')
        print('2. View All Books')
        print('3. Search Book')
        print('4. Remove Book')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            library.add_book()
        elif choice == '2':
            library.view_all_books()
        elif choice == '3':
            library.search_book()
        elif choice == '4':
            library.remove_book()
        elif choice == '5':
            print('Exit')
            break
        else:
            print('Invalid choice. Please try again.\n')

# Run the library management system
library_system()