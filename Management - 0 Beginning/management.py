# Initialize empty list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added successfully.')

def remove_task(task):
    tasks.remove(task)
    print(f'Task "{task}" removed successfully.')

def view_tasks():
    if tasks:
        print('Tasks:')
        for task in tasks:
            print(task)
    else:
        print('No tasks to display.')

def mark_complete(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" marked as complete.')
    else:
        print(f'Task "{task}" not found.')

# Main loop
while True:
    command = input('Enter a command (add, remove, view, complete, exit): ')

    if command == 'add':
        task = input('Enter a task to add: ')
        add_task(task)
    elif command == 'remove':
        task = input('Enter a task to remove: ')
        remove_task(task)
    elif command == 'view':
        view_tasks()
    elif command == 'complete':
        task = input('Enter a task to mark as complete: ')
        mark_complete(task)
    elif command == 'exit':
        print("Goodbye")
        break
    else:
        print('Invalid command.')

