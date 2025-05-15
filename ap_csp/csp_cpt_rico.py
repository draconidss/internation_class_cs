# Store all book information
books = []

# Function to add a book to the library
def add_book():
    # Prompt user for book title
    title = input("Please enter the title of the book: ")
    # Prompt user for book author
    author = input("Please enter the author of the book: ")
    # Create a book dictionary
    book = {
        "title": title,
        "author": author,
        "is_borrowed": False
    }
    # Add the book to the list
    books.append(book)
    print("Book added successfully!")

# Function to borrow a book from the library
def borrow_book():
    # Prompt user for the title of the book to borrow
    title = input("Please enter the title of the book to borrow: ")
    # Iterate through the books list
    for book in books:
        if book["title"] == title:
            if book["is_borrowed"]:
                print("This book has already been borrowed.")
            else:
                # Mark the book as borrowed
                book["is_borrowed"] = True
                print("Book borrowed successfully!")
                return
    print("The book was not found.")


# Function to return a book to the library
def return_book():
    # Prompt user for the title of the book to return
    title = input("Please enter the title of the book to return: ")
    # Iterate through the books list
    for book in books:
        if book["title"] == title:
            if not book["is_borrowed"]:
                print("This book has not been borrowed.")
            else:
                # Mark the book as returned
                book["is_borrowed"] = False
                print("Book returned successfully!")
                return
    print("The book was not found.")


# Main function to control the program flow
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        # Prompt user for a choice
        choice = input("Please enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        else:
            print("Invalid choice. Please try again.")


# Program entry point
if __name__ == "__main__":
    main()