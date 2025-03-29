def add_item(shopping_list, item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    # TODO: Append the item to the shopping list
   # Fill in this line

### Snippet 2: Function to View Items

def view_items(shopping_list):
    """Display all items in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Shopping List:")
        # TODO: Iterate through the shopping list and print each item
        for item in shopping_list:
        #for ______ in shopping_list:  # Fill in this line
            print(f"- {item}")  # Fill in this line

### Snippet 3: Main Function to Manage the Shopping List

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        print("\n--- Shopping List Manager ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)  # Call the function to add the item
        elif choice == '2':
            view_items(shopping_list)  # Call the function to view items
        elif choice == '3':
            print("Exiting the shopping list manager.")
            break  # Exit the loop
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()  # Start the shopping list manager