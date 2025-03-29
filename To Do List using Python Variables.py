def display_menu():
    """Display the main menu."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    """Add a new task to the list."""
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"description": description, "due_date": due_date, "completed": False})
    print("Task added.")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Current Tasks ---")
        for index, task in enumerate(tasks):
            status = "✔️" if task["completed"] else "❌"
            print(f"{index + 1}. {task['description']} (Due: {task['due_date']}) - Status: {status}")

def mark_task_complete(tasks):
    """Mark a task as complete."""
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    """Delete a task from the list."""
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()