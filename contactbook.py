import json

FILENAME = "contacts.json"


#load contacts
def load_contact():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        return {}
    

#save contacts
def save_contact(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f)
    
#add contacts
def add_contacts(name, phone):
    contacts = load_contact()
    contacts[name] = phone
    save_contact(contacts)
    print(f"your name {name} and your phone number {phone} have been added to the contact")

#view contacts
def view_contacts():
    contacts = load_contact()
    for name, phone in contacts.items():
        print(f"{name} : {phone}")

#cli menu
def menu():
    while True:
        print("\nContact Menu")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Exit")
        choice = input("Enter choice: ").strip()  # remove spaces
        if choice == "1":
            name = input("Enter your name: ")
            phone = input("Enter your phone number ")
            add_contacts(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            break
        else:
            print("you have entered an invalid choice")

if __name__ == "__main__":
    menu()

