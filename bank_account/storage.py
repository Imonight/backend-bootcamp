import json
import os

FILENAME = "bank.json"

def load_accounts():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump({}, f)
        return {}
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_accounts(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def save_account(name, balance):
    accounts = load_accounts()
    accounts[name] = balance
    save_accounts(accounts)

def get_account(name):
    accounts = load_accounts()
    return accounts.get(name)


