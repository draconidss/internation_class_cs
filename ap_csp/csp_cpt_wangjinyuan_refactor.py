# Library Management System

# Initialize the list with three books
library = [
    {"title": "book2", "author": "author2"},
    {"title": "book3", "author": "author3"},
    {"title": "book4", "author": "author4"}
]

def add_book(title, author):
    for book in library:
        if (book["title"].lower() == title.lower() and
            book["author"].lower() == author.lower()):
            print("This book already exists in the library!")
            return
    
    # Add new book
    new_book = {
        "title": title,
        "author": author
    }
    library.append(new_book)
    print("Book added successfully!")

def display_books():
    # Display all books in the library (optional feature)
    print("\nCurrent Library Inventory:")
    if not library:
        print("The library is empty!")
    else:
        for book in library:
            print("Title: " + book["title"], "Author: " + book["author"])

def main():
    # Main program loop
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Exit")
        
        choice = input("Please enter your choice (1-3): ")
        
        if choice == "1":
            title = input("Please enter the title of the book: ")
            author = input("Please enter the author of the book: ")
            add_book(title, author)
        elif choice == "2":
            display_books()
        elif choice == "3":
            print("Thank you for using the Library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()