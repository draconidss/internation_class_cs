# Library Management System

# Initialize an empty list to store books
library = []

def add_book():
    """Add a new book to the library"""
    title = input("Please enter the title of the book: ")
    author = input("Please enter the author of the book: ")
    
    # Check if book already exists
    for book in library:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("This book already exists in the library!")
            return
    
    # Add new book
    new_book = {
        "title": title,
        "author": author,
        "is_borrowed": False
    }
    library.append(new_book)
    print("Book added successfully!")

def borrow_book():
    """Borrow a book from the library"""
    title = input("Please enter the title of the book to borrow: ")
    
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            found = True
            if book["is_borrowed"]:
                print("This book has already been borrowed.")
            else:
                book["is_borrowed"] = True
                print("Book borrowed successfully!")
            break
            
    
    if not found:
        print("The book was not found.")

def return_book():
    """Return a book to the library"""
    title = input("Please enter the title of the book to return: ")
    
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            found = True
            if not book["is_borrowed"]:
                print("This book has not been borrowed.")
            else:
                book["is_borrowed"] = False
                print("Book returned successfully!")
            break
    
    if not found:
        print("The book was not found.")

def display_books():
    """Display all books in the library (optional feature)"""
    print("\nCurrent Library Inventory:")
    if not library:
        print("The library is empty!")
    else:
        for i, book in enumerate(library, 1):
            status = "Borrowed" if book["is_borrowed"] else "Available"
            print(f"{i}. {book['title']} by {book['author']} - {status}")

def main():
    """Main program loop"""
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display all books")
        print("5. Exit")
        
        choice = input("Please enter your choice (1-5): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()