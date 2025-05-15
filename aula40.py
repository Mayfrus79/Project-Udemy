import os

def list_tasks(tasks):
    print()
    if not tasks:
        print('No tasks to list')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()

def undo(tasks, redo_tasks):
    print()
    if not tasks:
        print('No tasks to undo')
        return

    task = tasks.pop()
    print(f'{task=} removed from the task list.')
    redo_tasks.append(task)
    print()

def redo(tasks, redo_tasks):
    print()
    if not redo_tasks:
        print('No tasks to redo')
        return

    task = redo_tasks.pop()
    print(f'{task=} added to the task list.')
    tasks.append(task)
    print()

def add_task(task, tasks):
    print()
    task = task.strip()
    if not task:
        print("You didn't type a task.")
        return
    print(f'{task=} added to the task list.')
    tasks.append(task)
    print()

tasks = []
redo_tasks = []

while True:
    print('Commands: list, undo, and redo')
    task_input = input('Enter a task or command: ')

    if task_input == 'list':
        list_tasks(tasks)
        continue
    elif task_input == 'undo':
        undo(tasks, redo_tasks)
        list_tasks(tasks)
        continue
    elif task_input == 'redo':
        redo(tasks, redo_tasks)
        list_tasks(tasks)
        continue
    elif task_input == 'clear':
        os.system('clear')
        continue
    else:
        add_task(task_input, tasks)
        list_tasks(tasks)
        continue
