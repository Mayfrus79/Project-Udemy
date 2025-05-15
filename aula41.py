import json
import os

# Function to list all tasks in the task list
def list_tasks(tasks):
    print()
    if not tasks:  # If no tasks exist, print a message
        print('No tasks to list')
        return
    print('Tasks:')
    for task in tasks:  # Print each task
        print(f'\t{task}')
    print()

# Function to undo the last added task, moving it to the redo list
def undo(tasks, redo_tasks):
    print()
    if not tasks:  # If there are no tasks to undo, print a message
        print('No task to undo')
        return
    task = tasks.pop()  # Remove the last task from the list
    redo_tasks.append(task)  # Add it to the redo list
    print(f'{task=} removed from the task list.')
    list_tasks(tasks)  # Display updated tasks

# Function to redo the last undone task, moving it back to the task list
def redo(tasks, redo_tasks):
    print()
    if not redo_tasks:  # If there are no tasks to redo, print a message
        print('No task to redo')
        return
    task = redo_tasks.pop()  # Remove the last task from the redo list
    tasks.append(task)  # Add it back to the task list
    print(f'{task=} added to the task list.')
    list_tasks(tasks)  # Display updated tasks

# Function to add a new task to the task list
def add_task(task, tasks):
    print()
    task = task.strip()  # Clean up any extra spaces around the task
    if not task:  # If the task is empty after stripping, show a message
        print('You did not enter a task.')
        return
    tasks.append(task)  # Add the task to the list
    print(f'{task=} added to the task list.')
    list_tasks(tasks)  # Display updated tasks

# Function to read tasks from a JSON file
def read(tasks, file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            return json.load(file)  # Load tasks from the file
    except FileNotFoundError:
        print('File does not exist')
        save(tasks, file_path)  # Create the file if it doesn't exist
    return tasks  # Return the current tasks

# Function to save tasks to the JSON file
def save(tasks, file_path):
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)  # Save tasks to the file

# Main program loop
FILE_PATH = 'tasks.json'
tasks = read([], FILE_PATH)  # Read tasks from file
redo_tasks = []  # Initialize redo list

while True:
    print('Commands: list, undo, and redo')  # Show available commands
    task_input = input('Enter a task or command: ')  # Ask user for input

    # Dictionary to map commands to functions
    commands = {
        'list': lambda: list_tasks(tasks),
        'undo': lambda: undo(tasks, redo_tasks),
        'redo': lambda: redo(tasks, redo_tasks),
        'clear': lambda: os.system('clear'),  # Clear screen command
        'add': lambda: add_task(task_input, tasks),
    }

    # Execute the corresponding function based on the input
    command = commands.get(task_input) if commands.get(task_input) else commands['add']
    command()

    # Save tasks to the file after each operation
    save(tasks, FILE_PATH)
