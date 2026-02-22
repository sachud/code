# FULL PYTHON CODE (Type this daily)
# ============================================
# PERSONAL TASK MANAGER (COMMAND LINE APP)
# ============================================

# This program allows a user to:
# 1. Add tasks
# 2. View tasks
# 3. Mark tasks as completed
# 4. Delete tasks
# 5. Save tasks to a file
# 6. Load tasks from a file

# --------------------------------------------
# Import required module
# --------------------------------------------
import json  # Used to save and load tasks from a file


# --------------------------------------------
# Global variable to store tasks
# Each task is a dictionary
# --------------------------------------------
tasks = []


# --------------------------------------------
# Function to load tasks from file
# --------------------------------------------
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []  # If file not found, start fresh


# --------------------------------------------
# Function to save tasks to file
# --------------------------------------------
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# --------------------------------------------
# Function to add a new task
# --------------------------------------------
def add_task():
    title = input("Enter task title: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("✅ Task added successfully!")


# --------------------------------------------
# Function to display all tasks
# --------------------------------------------
def view_tasks():
    if not tasks:
        print("📭 No tasks available.")
        return

    for index, task in enumerate(tasks):
        status = "✔ Completed" if task["completed"] else "❌ Pending"
        print(f"{index + 1}. {task['title']} - {status}")


# --------------------------------------------
# Function to mark a task as completed
# --------------------------------------------
def complete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to complete: "))
        tasks[task_number - 1]["completed"] = True
        print("🎉 Task marked as completed!")
    except (ValueError, IndexError):
        print("⚠ Invalid task number!")


# --------------------------------------------
# Function to delete a task
# --------------------------------------------
def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"🗑 Task '{removed_task['title']}' deleted.")
    except (ValueError, IndexError):
        print("⚠ Invalid task number!")


# --------------------------------------------
# Main menu function
# --------------------------------------------
def menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


# --------------------------------------------
# Main program loop
# --------------------------------------------
def main():
    load_tasks()  # Load tasks when program starts

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("💾 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


# --------------------------------------------
# Program entry point
# --------------------------------------------
if __name__ == "__main__":
    main()

'''
FEATURES TO ADD (One Per Day)
🟢 Beginner Add-ons

Add task priority (High / Medium / Low)
Add task creation date
Confirm before deleting a task
Count completed vs pending tasks

🟡 Intermediate Add-ons

Search tasks by name
Sort tasks by priority
Separate completed & pending views
Auto-save after every action

🔵 Advanced Add-ons

User login system (username-based tasks)
Password protection
Convert to GUI (Tkinter)
Convert to REST API (Flask)
'''