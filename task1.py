
tasks = []

while True:
    
    print("\nTODO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")
        
    elif choice == '2':
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")
            
    elif choice == '3':
        if tasks:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                completed_task = tasks.pop(task_number - 1)
                print(f"'{completed_task}' marked as completed.")
            else:
                print("Invalid task number.")
        else:
            print("No tasks in the list.")
    
    elif choice == '4':
        break
    
    else:
        print("Invalid choice. Please select a valid option.")