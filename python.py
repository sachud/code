# Complete Beginner-Friendly Python Code (Type Daily)
# Programming Language: Python
# Code Functionality: Command-Line To-Do List Manager
'''
This program lets you:

Add tasks

View tasks

Mark tasks as completed

Delete tasks

It uses basic Python only (variables, lists, loops, functions, input/output).
'''
# -------------------------------
# SIMPLE TO-DO LIST APPLICATION
# -------------------------------

# This list will store all tasks
# Each task will be a dictionary with name and status
tasks = []

# Function to add a new task
def add_task():
    task_name = input("Enter task name: ")
    
    # Create a task as a dictionary
    task = {
        "name": task_name,
        "completed": False
    }
    
    # Add task to the list
    tasks.append(task)
    print("Task added successfully!\n")


# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
        return

    print("\nYour Tasks:")
    
    # Loop through all tasks
    for index, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index + 1}. {task['name']} - {status}")
    
    print()  # Empty line for readability


# Function to mark a task as completed
def complete_task():
    view_tasks()
    
    if len(tasks) == 0:
        return

    task_number = int(input("Enter task number to mark as completed: "))
    
    # Convert to index (list index starts from 0)
    index = task_number - 1

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!\n")
    else:
        print("Invalid task number.\n")


# Function to delete a task
def delete_task():
    view_tasks()
    
    if len(tasks) == 0:
        return

    task_number = int(input("Enter task number to delete: "))
    index = task_number - 1

    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Deleted task: {deleted_task['name']}\n")
    else:
        print("Invalid task number.\n")


# Main menu function
def show_menu():
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


# Main program loop
def main():
    while True:
        show_menu()
        
        choice = input("Enter your choice (1-5): ")
        print()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Happy Coding 🚀")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Start the program
main()

'''
How to Practice This Daily

Type the entire code manually (don’t copy-paste)
Run it
Change small things:
    Rename variables
    Add print statements
    Modify menu text


Features You Can Add (Practice Roadmap)
🟢 Beginner Additions

Add task priority (High / Medium / Low)
Ask for confirmation before deleting
Count and display total tasks

🟡 Intermediate Additions

Save tasks to a file (text or JSON)
Load tasks automatically when program starts
Add due dates

🔵 Advanced Additions (Later)

Convert to a GUI app (Tkinter)
Convert to a web app (Flask)
Add user login system
Store tasks in a database (SQLite)
'''