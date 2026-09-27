"""Simple to-do list — uses lists, loops, and functions."""

todos = []

def show_todos():
    if not todos:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")

def add_task(task):
    todos.append(task)

while True:
    print("\nMenu: 1) Add task, 2) View, 3) Quit")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            add_task(task)
        else:
            print("Task cannot be empty.")
    elif choice == "2":
        show_todos()
    elif choice == "3":
        break
    else:
        print("Invalid option — please choose 1, 2, or 3.")
