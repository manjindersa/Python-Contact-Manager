# Python Contact Manager

## Description
The Python Contact Manager is a simple command-line application that allows users to manage a list of contacts. Users can view, add, delete, and list contacts through an easy-to-use command menu.

## Features
- **List Contacts**: Display all contacts in the contact list.
- **View Contact**: View details of a specific contact.
- **Add Contact**: Add a new contact to the list.
- **Delete Contact**: Delete an existing contact from the list.
- **Exit Program**: Exit the contact manager application.

## Usage
1. **Clone the Repository**: Clone the repository to your local machine.
    ```sh
    git clone https://github.com/yourusername/Python-Contact-Manager.git
    ```
2. **Navigate to the Directory**: Change to the directory containing the `ContactManager.py` file.
    ```sh
    cd Python-Contact-Manager
    ```
3. **Run the Program**: Execute the Python script.
    ```sh
    python ContactManager.py
    ```
4. **Use the Command Menu**:
    - `list`: Display all contacts.
    - `view`: View a specific contact by its number.
    - `add`: Add a new contact.
    - `del`: Delete a contact by its number.
    - `exit`: Exit the program.

## Example
```
Contact Manager

COMMAND MENU

list - Display all contacts
view - View a contact
add  - Add a contact
del  - Delete a contact
exit - Exit program

Command: list
1. Gurjinder Singh
2. Amandeep Singh

Command: view
Number: 1
Name: Gurjinder Singh
Email: gurjinder@gmail.com
Phone: +91 9065465000

Command: add
Name: Manjinder Singh
Email: manjinder@gmail.com
Phone: +91 9045454545
Manjinder Singh was added.

Command: del
Number: 2
Amandeep Singh was deleted.

Command: exit
Bye!
```

## Code Structure

### Main Program
- **contacts**: A list of contacts, where each contact is represented as a list containing the name, email, and phone number.
- **Command Menu**: A loop that continuously prompts the user for commands and executes the corresponding actions.

### Commands
- **list**: Displays all contacts.
- **view**: Prompts for a contact number and displays the corresponding contact's details.
- **add**: Prompts for the contact's name, email, and phone number, then adds the new contact to the list.
- **del**: Prompts for a contact number and deletes the corresponding contact from the list.
- **exit**: Exits the program.

## Author
- **Manjinder Singh**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, report issues, or suggest features by opening a pull request or issue on the [GitHub repository](https://github.com/manjindersa/Python-Contact-Manager).
