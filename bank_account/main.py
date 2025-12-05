from bank import Bank

bank = Bank()

def menu():
    while True:
        print("Welcome to EazyBrave Bank")
        print("1. Create Account")
        print("2. deposit")
        print("3. withdrawal")
        print("4. check balance")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            balance = int(input("Enter your balnce: "))
            bank.create_account(name, balance)
            print(f"{name} you have successfully created an account")
        elif choice == "2":
            name = input("Enter your name: ")
            amount = int(input("Enter the deposit amount: "))
            bank.deposit(name, amount)
            print(f"you have deposit {amount} to your account")
        elif choice == "3":
            name = input("Enter your name: ")
            amount = int(input("Enter your withdrawal: "))
            bank.withdrawal(name, amount)
            print(f"your withdrawal of {amount} was successful")
        elif choice == "4":
            name = input("Enter your name: ")
            balances = bank.check_balance(name)
            print(f"your account balance is {balances}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("invalid input")

if __name__ == '__main__':
    menu()


