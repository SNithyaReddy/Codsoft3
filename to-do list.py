# Simple To-Do List Application

# Global list to store tasks
todo_list = []

# Function to display the current to-do list
def display_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\n--- Your To-Do List ---")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

# Function to add a new task to the list
def add_task():
    task = input("\nEnter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to update an existing task
def update_task():
    display_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number you want to update: "))
            if 1 <= task_number <= len(todo_list):
                updated_task = input("Enter the updated task: ")
                todo_list[task_number - 1] = updated_task
                print(f"Task {task_number} updated successfully.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    display_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number you want to delete: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

# Main function to interact with the user
def todo_app():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option from 1 to 5.")

# Run the To-Do List application
todo_app()
