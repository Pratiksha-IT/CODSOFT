def main():
    tasks = []
    while True:
        print("=====================")
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Complete Tasks")
        print("4.Exits")
        print("=====================")
        choice=int(input("Enter your choice:"))

        if choice==1:
            print()
            print("======================")
            task_no=int(input("Enter the number of tasks:"))
            for i in range(task_no):
                task=input("Enter the task:")
                tasks.append({"task" : task, "Done" : False})
                print("Task added sucessfully!")
                print("======================")

        elif choice==2:
            print()
            if not tasks:
                print("**No tasks available**")
                print(" Please add tasks First  ")
            else:
                print("======================")
                print("\nTask:")
                for index, task in enumerate(tasks):    
                    status="Done" if task["Done"] else "Not Done"
                    print(f"{index+1}. {task['task']} -{status}")
                    print("======================")  

        elif choice==3:
            print()
            if not tasks:
                print("**No tasks available**")
                print(" Please add tasks First")
            else:
                print("======================")
                task_no=int(input("Enter the task number that has to be marked as done:"))
                if 0<task_no<=len(tasks):
                    tasks[task_no-1]["Done"]=True
                    print(f"task {task_no} marked as done.")
                    print("======================")
                else:
                    print("Invalid task number,Please try again.")

        elif choice==4:
            print()
            print("======================")
            print("Exiting the To-Do list,Goodbye!")
            break

        else:
            print("Invalid Choice,Please Try again.")

if __name__ == "__main__":
    main()

            

