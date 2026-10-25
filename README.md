
# Python CLI To-Do List Manager

## Project Overview

This project is a command-line application developed in Python.
It allows users to add, view, complete, and remove tasks.

Tasks are saved in a JSON file so that they remain available
after the program is restarted.

## Features

- Add tasks
- View all tasks
- Mark tasks as completed
- Remove tasks
- Save tasks automatically
- Validate user input
- Handle errors gracefully
- Automated unit tests

## Requirements

- Python 3.9 or newer recommended
- No external packages required

## Project Structure

- main.py: Command-line menu and user interaction
- task_manager.py: Task operations and file storage
- test_task_manager.py: Automated tests
- README.md: Project documentation
- tasks.json: Automatically created data file

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

   python main.py

4. Select an option from the menu.

## How to Run Tests

Run:

   python -m unittest -v
5. Error while running the program
## If the program is not running so refresh the vs and open terminal(new terminal) and enter this

    cd ToDoListManager

    then 

    python main.py

## Design Decisions

The application uses a TaskManager class to organize
task-related operations.

The menu and task logic are separated into different files
to improve readability and maintainability.

JSON is used for storage because it is simple and included
in Python's standard library.

Each task receives a unique integer ID. This makes it
possible to remove or complete a task without relying
on its position in the list.

Input validation prevents blank task descriptions,
invalid menu choices, and invalid task IDs.

## Logic Flow

1. Start the application.
2. Load saved tasks.
3. Display the menu.
4. Read the user's choice.
5. Validate the input.
6. Perform the selected task operation.
7. Save changes to the JSON file.
8. Return to the menu.
9. Exit when the user selects option 5.

## Manual Testing

1. Add a task and verify that it appears.
2. View the task list.
3. Mark a task as completed.
4. Remove a task.
5. Try adding an empty task.
6. Enter an invalid menu choice.
7. Enter a non-numeric task ID.
8. Restart the application and verify that tasks remain saved.

## Future Improvements

- Add task priorities
- Add due dates
- Search tasks
- Edit existing tasks
- Add task categories

## Dependencies

Only Python standard-library modules are used.
No third-party installation is necessary.
