# Outside functions --->

# A function to add tasks -->
def add_task(todo_list):
    task = input("Please enter your task: ")
    todo_list.append(task)
    print(f"Your new task {task} was just added to the list.")
    
def view_tasks(todo_list):
    # index and task both iterated
    for index, task in enumerate(todo_list, start=1): 
        print(f"{index}) {task}")
        

def remove_task(todo_list):
    if not todo_list:
            print("There are no tasks assigned yet!")
            return view_tasks(todo_list)
    try:
        view_tasks(todo_list)
        dltask = int(input("What task do you want to be removed? Enter the number: ")) - 1
        removed_task = todo_list.pop(dltask)
        print(f"Task: {removed_task} was removed from tasks!")
    except ValueError:
        print("Please enter integers only!")


def main():
    # This is the main function where the core logic of your program resides
    todo_list = []

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            remove_task(todo_list)
        elif choice == '3':
            view_tasks(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This conditional checks if the script is being run directly or being imported
if __name__ == "__main__":
    main()
