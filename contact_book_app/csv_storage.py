import csv

FILENAME = "contacts.csv"


def save_to_csv(data: dict):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Names", "Phone"])
        for name, phone in data.items():
            writer.writerow([name, phone])


def load_from_csv():
    contacts = {}
    try:
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts[row["Name"]] = contacts[row["phone"]]
    except FileExistsError:
        pass
    return contacts
