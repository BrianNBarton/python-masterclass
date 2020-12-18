# function to display the application title
def display_title():
    print("Contact Manager")
    print()


# function to display the user menu
def display_menu():
    print("COMMAND MENU")
    print("list - Display contacts")
    print("view - View contacts")
    print("add  - Add contact")
    print("del  - Delete contact")
    print("exit - Exit")
    print()


# function to unpack the contact list and print contents to the console
def get_list(contact_list):
    for i, contact in enumerate(contact_list, start=1):
        print(str(i) + ". " + contact[0])
    print()


# function to view a specific contact
def view(contact_list):
    # user selection
    number = int(input("Number: "))
    # test if contact si in list if not display error message
    if number < 1 or number > len(contact_list):
        display_error_message()

    else:
        i = 1
        # contact selection structure
        for contact in contact_list:
            if number == i:
                print("Name: " + contact[0])
                print("Email: " + contact[1])
                print("Phone: " + contact[2])
                print()
                return
            else:
                i += 1


# function to add contacts to the list
def add(contact_list):
    # initialize new contact
    contact = []
    # get contact attributes
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    # append attributes to contact
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    # append contact to contacts
    contact_list.append(contact)
    print(contact[0] + " was added.")
    print()


# function to delete contacts from the list
def delete(contact_list):
    # user selects contact
    number = int(input("Number: "))
    # test if contact is in list
    if number < 1 or number > len(contact_list):
        display_error_message()

    else:

        contact = contact_list.pop(number - 1)
        print(contact[0] + " was deleted.")
        print()


# function to diaplay the error message
def display_error_message():
    print("You entered an invalid contact number!")
    print()


# main function
def main():
    # initialize contacts list
    contact_list = [["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"],
                    ["Mike Murach", "mike@murach.com", "559-123-4567"]]

    display_title()
    display_menu()

    # main control loop
    while True:
        # get command
        command = input("command: ")

        # drop user input through selection block
        if command.lower() == "list":
            get_list(contact_list)
        elif command.lower() == "view":
            view(contact_list)
        elif command.lower() == "add":
            add(contact_list)
        elif command.lower() == "del":
            delete(contact_list)

        else:
            break
    print("Bye!")


# test if this module contains main function for the application
if __name__ == "__main__":
    main()
