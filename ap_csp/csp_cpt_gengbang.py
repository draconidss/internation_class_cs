# Initialize some fruits (excluding apples)
fruits = {
    "Banana": 10,
    "Orange": 15,
    "Grapes": 20,
    "Mango": 5
}

# Store fruit
def store_fruit(name, quantity):
    fruits[name] = quantity
    print(f"Stored {quantity} {name}(s).")

# Take fruit
def take_fruit(name, quantity):
    found = False
    for fruit_name in fruits:
        if fruit_name == name:
            fruits[name] -= quantity  # Reduce the quantity
            if fruits[name] <= 0:
                del fruits[name]  # Remove the fruit if quantity is zero or negative
            return
    print(f"{name} does not exist in the inventory.")
    

# Display all fruits and their quantities
def display_inventory():
    print("\nCurrent Fruit Inventory:")
    if fruits:
        for name, quantity in fruits.items():
            print(f"{name}: {quantity}")
    else:
        print("The inventory is empty.")

# Main program
def main():
    print("Initial Fruit Inventory:")
    display_inventory()
    
    while True:
        print("\nFruit Warehouse Management System")
        print("1. Store Fruit")
        print("2. Take Fruit")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter the fruit name: ")
            quantity = int(input("Enter the quantity: "))
            store_fruit(name, quantity)
        elif choice == "2":
            name = input("Enter the fruit name to take: ")
            quantity = int(input("Enter the quantity to take: "))
            take_fruit(name, quantity)
        elif choice == "3":
            print("Exiting the Fruit Warehouse Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        display_inventory()

# Program entry point
if __name__ == "__main__":
    main()