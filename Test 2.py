# Define an empty dictionary to store phone directory
phoneDirectory = {}
print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY")

# Display the menu and get user input
while True:
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    # Add a new record
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record added successfully")
        print("menu")

    # Search for a record
        print("Menu")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in phoneDirectory:
            print("Phone number:", phoneDirectory[name])
        else:
            print("Record not found")
           

    # Update a record
        print("Menu")
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in phoneDirectory:
            phone = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = phone
            print("Record updated successfully")
        else:
            print("Record not found")

    # Delete a record
        print("Menu")
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted successfully")
        else:
            print("Record not found")
           
    # Quit the program
        print("Menu")
    elif choice == "5": 
        print("Thank you for using Grann's Phone Directory")
        
        break

    # Handle invalid input
    else:
        print("Invalid choice. Please try again")
