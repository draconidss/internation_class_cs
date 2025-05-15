# Store all book information
books = [
    
    {"title": "1984", "is_borrowed": False},
    {"title": "The Great Gatsby", "is_borrowed": False},
    {"title": "Pride and Prejudice", "is_borrowed": False},
    {"title": "The Catcher in the Rye", "is_borrowed": False}
]

# Function to borrow a book from the library
def borrow_book(title):
    for book in books:
        if book["title"] == title:
            if book["is_borrowed"]:
                print("This book has already been borrowed.")
            else:
                book["is_borrowed"] = True
                print("Book borrowed successfully!")
            return
    print("The book was not found.")

# Function to return a book to the library
def return_book(title):
    for book in books:
        if book["title"] == title:
            if book["is_borrowed"]:
                book["is_borrowed"] = False
                print("Book returned successfully!")
            else:
                print("This book has not been borrowed.")
            return
    print("The book was not found.")

# Main function to control the program flow
def main():
    # Display all book titles
    print("\nCurrent Library Inventory:")
    for book in books:
        print("《" + book["title"] + "》")
    while True:
        print("\nLibrary Management System")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter the title of the book to borrow: ")
            borrow_book(title)
        elif choice == "2":
            title = input("Enter the title of the book to return: ")
            return_book(title)
        elif choice == "3":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Program entry point
if __name__ == "__main__":
    main()