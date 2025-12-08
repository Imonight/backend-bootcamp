from storage import load_todos, save_todos
from utils import log_action, validate_input


@log_action
@validate_input
def add_tasks(tasks):
    todos = load_todos()
    todos.append(tasks)
    save_todos(todos)
    print("Your task have been added")


@log_action
def view_tasks():
    todos = load_todos()
    if todos == []:
        print("There is no To-do lists available")
    else:
        print("Your task(s)")
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")


@log_action
def delete_tasks(index):
    view_tasks()
    todos = load_todos()
    if index >= 0 and index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"you removed {removed} from the list")
    else:
        print("Invalid choice")
