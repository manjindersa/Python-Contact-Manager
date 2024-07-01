contacts = [
    ["Gurjinder Singh", "gurjinder@gmail.com", "+91 9065465000"],
    ["Amandeep Singh", "amandeep@gmail.com", "+91 9058475000"]
]

print("\nContact Manager\n")
print("COMMAND MENU\n")
print("list - Display all contacts")
print("view - View a contact")
print("add  - Add a contact")
print("del  - Delete a contact")
print("exit - Exit program")

while True:
    command = input("\nCommand: ").strip().lower()
    
    if command == "list":
        if contacts:
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact[0]}")
        else:
            print("No contacts found.")
    
    elif command == "view":
        try:
            number = int(input("Number: "))
            if number < 1 or number > len(contacts):
                print("Invalid contact number.")
            else:
                contact = contacts[number - 1]
                print(f"Name: {contact[0]}")
                print(f"Email: {contact[1]}")
                print(f"Phone: {contact[2]}")
        except ValueError:
            print("Invalid input; please enter a valid contact number.")
    
    elif command == "add":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        contacts.append([name, email, phone])
        print(f"{name} was added.")
    
    elif command == "del":
        try:
            number = int(input("Number: "))
            if number < 1 or number > len(contacts):
                print("Invalid contact number.")
            else:
                contact = contacts.pop(number - 1)
                print(f"{contact[0]} was deleted.")
        except ValueError:
            print("Invalid input; please enter a valid contact number.")
    
    elif command == "exit":
        print("Bye!")
        break
    
    else:
        print("Invalid command. Please try again.\n")
