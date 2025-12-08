import json
import os

FILENAME = "bank.json"


def load_accounts():
    try:
        if not os.path.exists(FILENAME):
            with open(FILENAME, "w") as f:
                json.dump({}, f)
            return {}
        with open(FILENAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("❌ Corrupted JSON file — resetting storage.")
        save_accounts({})
        return {}

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {}


def save_accounts(data):
    try:
        with open(FILENAME, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"error saving account: {e}")


def save_account(name, balance):
    accounts = load_accounts()
    accounts[name] = balance
    save_accounts(accounts)


def get_account(name):
    accounts = load_accounts()
    return accounts.get(name)
