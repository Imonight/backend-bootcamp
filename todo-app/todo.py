from tasks import add_tasks, view_tasks, delete_tasks

def menu():
    while True:
        print("\nWelcome to the Menu")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Exit")

        choice = (input("Enter your choice: "))

        if choice == "1":
            tasks = (input("Enter your tasks: "))
            add_tasks(tasks)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = input("choose from the task you want to delete: ")
            if index.isdigit():
                delete_tasks(int(index)-1)
            else:
                print("Error: must be a number")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()


        
        

        






    




