# Simple To-Do List in Python

tasks = []  # empty list to store tasks

while (2):
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add Task
        task = input("Enter the task: ")
        tasks.append(task)  # add task to the list
        print(f"✅ '{task}' added to the list.")

    elif choice == "2":
        # Remove Task
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)  # remove if found
            print(f"🗑️ '{task}' removed from the list.")
        else:
            print("⚠️ Task not found!")

    elif choice == "3":
        # View Tasks
        if len(tasks) == 0:
            print("📭 No tasks in the list.")
        else:
            print("\n📋 Your Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

    elif choice == "4":
        # Exit the program
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Please select 1-4.")
