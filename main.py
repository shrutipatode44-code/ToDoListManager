from task_manager import TaskManager
def display_menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Remove a task")
    print("5. Exit")
    print("==============================")

def show_tasks(manager):
    tasks = manager.get_tasks()

    if not tasks:
        print("Your task list is empty.")
        return

    print("\nYour Tasks:")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(
            f'ID: {task["id"]} | '
            f'{task["title"]} | {status}'
        )

def read_task_id():
    try:
        task_id = int(input("Enter task ID: "))

        if task_id <= 0:
            print("Task ID must be a positive number.")
            return None

        return task_id

    except ValueError:
        print("Invalid input. Enter a whole number.")
        return None

def main():
    try:
        manager = TaskManager()
    except RuntimeError as error:
        print(f"Unable to load tasks: {error}")
        return

    print("Welcome to your To-Do List Manager!")

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                title = input("Enter task description: ")
                task = manager.add_task(title)
                print(f"Task added! ID: {task['id']}")

            elif choice == "2":
                show_tasks(manager)

            elif choice == "3":
                show_tasks(manager)

                if manager.get_tasks():
                    task_id = read_task_id()

                    if task_id is not None:
                        task = manager.complete_task(task_id)
                        print(f"Completed: {task['title']}")

            elif choice == "4":
                show_tasks(manager)

                if manager.get_tasks():
                    task_id = read_task_id()

                    if task_id is not None:
                        task = manager.remove_task(task_id)
                        print(f"Removed: {task['title']}")

            elif choice == "5":
                print("Tasks saved. Goodbye!")
                break

            else:
                print("Invalid choice. Select a number from 1 to 5.")

        except ValueError as error:
            print(f"Error: {error}")

        except RuntimeError as error:
            print(f"File error: {error}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
