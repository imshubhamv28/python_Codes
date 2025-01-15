def displayMenu():
    print("\nPhonebook Menu")
    print("1.Search for a Contact")
    print("2.Add a New Contact Number")
    print("3.delete a Contact Number")
    print("4.List of all Contact Numbers")
    print("5.Exit")


def searchContact(phonebook):
    name = input("Add a contact : ").strip()
    if name in phonebook:
        print(f"Contact found-{name}:{phonebook[name]}")
    else:
        print(f"Contact {name} is Not Exist")


def addContact(phonebook):
   name = input("Enter to add a Contact:").strip()
   if name in phonebook:
       print(f"Contact {name} is already in the Phonebook List")
   else:
       number = input("Add contact Number:")
       phonebook[name] = number
       print(f"Contact {name} is added successfully")

def deleteContact(phonebook):
    name = input("Enter Contact name to delete:")
    if name in phonebook:
        del phonebook[name]
        print(f"contact {name} is deleted succesfully")
    else:
        print(f"Contact {name} not Found")


def contactList(phonebook):
    if phonebook:
        print("\nPhonebook List")
        for name,number in phonebook.items():
            print(f"{name}:{number}")
    else:
        print("Phonebook is Empty")

    
def main():
    phonebook = {}

    while True:
        displayMenu()
        option = input("Enter to choose an Option:")

        if option == "1":
            searchContact(phonebook)
        elif option == "2":
            addContact(phonebook)
        elif option == "3":
            deleteContact(phonebook)
        elif option == "4":
            contactList(phonebook)
        elif option == "5":
            print("Exiting phonebook...Goodby!")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()

            





    