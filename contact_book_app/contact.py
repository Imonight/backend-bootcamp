from storage import load_contact, save_contact
from util import validate_input, log_action


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    @log_action
    @validate_input
    def add_contact(self):
        contact = load_contact()
        contact[self.name] = self.phone
        save_contact(contact)
        print(f"contact saved {self.name} - {self.phone}")
    
    
    @staticmethod
    @log_action
    def view_contact():
        contact = load_contact()
        if not contact:
            print("There is no contact")
            return
        
        print("Contact Lists")

        for name, phone in contact.items():
            print(f"{name} : {phone}")
            

    