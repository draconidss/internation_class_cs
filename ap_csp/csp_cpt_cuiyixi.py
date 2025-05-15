library = ["book2", "book3", "book4"]

def add_book(title):
    for book in library:
        if book.lower() == title.lower():
            print("This book already exists in the library!")
            return
    
    library.append(title)
    print("Book added successfully!")

def delete_book(title):
    for book in library:
        if book.lower() == title.lower():
            library.remove(book)
            print("Book deleted successfully!")
            return
    print("Book not found in the library!")

def display_books():
    print("\nCurrent Library Inventory:")
    if not library:
        print("The library is empty!")
    else:
        for book in library:
            print(book)

def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Display all books")
        print("4. Exit")
        
        choice = input("Please enter your choice (1-4): ")
        
        if choice == "1":
            title = input("Please enter the title of the book: ")
            add_book(title)
        elif choice == "2":
            title = input("Please enter the title of the book to delete: ")
            delete_book(title)
        elif choice == "3":
            display_books()
        elif choice == "4":
            print("Thank you for using the Library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()