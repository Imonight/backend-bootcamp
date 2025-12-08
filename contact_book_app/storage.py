import json

FILENAME = "contact.json"


def load_contact():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not Found")
        return {}


def save_contact(contact):
    with open(FILENAME, "w") as f:
        json.dump(contact, f, indent=4)
