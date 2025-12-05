from storage import save_account, get_account

class Bank:
    def create_account(self, name, balance=0):
        if get_account(name) is not None:
            return "Account Already Exists"
        save_account(name,balance)
        return f"Account name {name} have been Created!"

    def deposit(self, name, amount):
        balance = get_account(name)
        if balance is None:
            return"Account Not Found"
        new_balance = balance + amount
        save_account(name, new_balance)
        return f"{name} your deposit of {amount} is successful, current balance {new_balance}"
    
    def withdrawal(self, name,amount):
        balance = get_account(name)
        if balance is None:
            return "Account Not Found"
        if amount > balance:
            return "Insufficient funds"
        new_balance = balance - amount
        save_account(name, new_balance)
        return f"{name} your withdrawal of {amount} is successful, current balance {new_balance}"
        
    def check_balance(self, name):
        balance = get_account(name)
        if balance is None:
            return "Account Not Found"
        return f"{name} Your current balance is {balance}"


