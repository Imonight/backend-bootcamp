import json

FILENAME = "todo.json"  # name the json file


# create a pythin file from json or converst json to python
def create_todo():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        return []


# save the todo task    or write to your json file
def save_todo(todo):
    with open(FILENAME, "w") as f:
        json.dump(todo, f)


# ad to the todo list
def add_todo(task):
    todo = create_todo()
    todo.append(task)
    save_todo(todo)
    print(f"your task {task} have been added to your To-Do")


# view todo list
def view_todo():
    todo = create_todo()
    if todo == []:
        print("No task is found")
        return
    for i, task in enumerate(todo, start=1):
        print(f"{i}. {task}")


# remove a task from the todo list
def remove_task(index):
    todo = create_todo()
    if index >= 0 and index < len(todo):
        removed = todo.pop(index)
        save_todo(todo)
        print(f"You have removed {removed} from the list")
    else:
        print("You have inputed an invalid task")


# runs the program
def menu():
    while True:
        print("\nWelcome to the menu")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Add your task: ")
            add_todo(task)
        elif choice == "2":
            view_todo()
        elif choice == "3":
            view_todo()
            index = int(input("Choose the task you want to remove: ")) - 1
            remove_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()
