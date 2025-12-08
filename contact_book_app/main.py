from contact import Contact


def menu():
    while True:
        print("\nWelcome! Menu")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            phone = input("Enter your Contact Phone: ")
            contact = Contact(name, phone)
            contact.add_contact()
        elif choice == "2":
            Contact.view_contact()
        elif choice == "3":
            keyword = input("Enter your search keyword: ")
            Contact.search_contact(keyword)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    menu()
