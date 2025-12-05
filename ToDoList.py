tasks=[" ",]
# print("__________________")
# print("|    ToDoList    |")
# print("------------------")
while(1):
    print()
    print("Enter 1. to add a new task: ")
    print("Enter 2. to remove a task: ")
    print("Enter 3. to show the task: ")
    print("Enter 4. to exit: ")
    print()
    try:
        choice=int(input("Enter number 1-4: "))
        if choice==1:
            task=input("Enter a task: ")
            tasks.append(task)
            print(f'{task} is added as task+.')
    
        elif choice==2:
            task=(input("Enter the task which you want to remove: "))
            if task in tasks:
                tasks.remove(task)
                print(f"'{task}' has removed successfully.")
            else:
                 print(f"{task} not found in the task list.")

        elif choice==3:
                print()
                print("____________________")
                print("     TO DO LIST     ")
                print("--------------------")
                for i in range (1,len(tasks)):
                    print(tasks[i])

        elif choice==4:
            break

        else:
            print("Invalid input please enter a number in between 1-4.")

    except:
         print("Please enter 1,2,3,4. Not something else!!")     

print("Thank you! Visit again.")