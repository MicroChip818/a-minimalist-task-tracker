import json
import sys
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_PATH = os.path.join(BASE_DIR, "tasks.json")

if len(sys.argv) < 2: # Invalid command due to commands taking at least 2 arguments
     print('Please enter a valid command')
     exit()

def now(): # Current date and time, formatted
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_tasks(tasks): # Saves the Python list of tasks into the tasks.json file
    with open(FILE_PATH, 'w') as f:
        json.dump(tasks, f, indent=4)

def load_tasks(): # Loads the JSON file into a Python list; creates the file if none exists before loading
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        save_tasks([])
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    
def add_task(tasks, description): # Adds a task
    if tasks:
        task_id = max((task["id"] for task in tasks)) + 1
    else:
        task_id = 1 # Default ID
    tasks.append({ # Appends a dictionary consisting of each attribute
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': now()})
    print(f"task added | id {task_id}") # Prints custom message based on the command
    return tasks  

def update_task(tasks, task_id, new_description): # Updates a task
    for task in tasks: # Iterates through each task until target task
        if task['id'] == int(task_id): # Converts ID from str to int
            task['description'] = new_description
            task['updatedAt'] = now()
            print(f"task updated | id {task_id}")
            return tasks
    print('404 | id not found')
    return tasks

def delete_task(tasks, task_id): # Deletes a task
    for task in tasks:
        if task['id'] == int(task_id):
            tasks.remove(task)
            print(f"task deleted | id {task_id}")
            return tasks
    print('404 | id not found')
    return tasks

def mark_in_progress(tasks, task_id): # Marks a task in-progress
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = 'in-progress'
            print(f"task marked in-progress | id {task_id}") 
            return tasks
    print('404 | id not found')
    return tasks

def mark_done(tasks, task_id): # Marks a task done
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = 'done'
            print(f"task marked done | id {task_id}")
            return tasks
    print('404 | id not found')
    return tasks

def list(tasks): # Prints every task
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['description']} | status: {task['status']} | id {task['id']}")

def list_todo(tasks): # Prints every task in-progress
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'todo':
            print(f"{task['description']} | id {task['id']}")

def list_in_progress(tasks):
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'in-progress':
            print(f"{task['description']} | id {task['id']}")

def list_done(tasks): # Prints every task that is done
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'done':
            print(f"{task['description']} | id {task['id']}")

def main(): # Main function
    tasks = load_tasks() # Loads the JSON file upon entering a command
    if sys.argv[1] == 'add': # argument at index 1
        add_task(tasks, sys.argv[2]) # argument at index 2
    elif sys.argv[1] == 'update':
        update_task(tasks, int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == 'delete':
        delete_task(tasks, int(sys.argv[2]))
    elif sys.argv[1] == 'mark-in-progress':
        mark_in_progress(tasks, int(sys.argv[2]))
    elif sys.argv[1] == 'mark-done':
        mark_done(tasks, int(sys.argv[2]))
    elif sys.argv[1] == 'list':
        list(tasks)
    elif sys.argv[1] == 'list-done':
        list_done(tasks)
    elif sys.argv[1] == 'list-todo':
        list_todo(tasks)
    elif sys.argv[1] == 'list-in-progress':
        list_in_progress(tasks)
    else:
        print('Please enter a valid command')
        exit() # Exits the program if no valid command is given
    save_tasks(tasks) # Saves the list into the JSON file
    pass

if __name__ == "__main__":
    main()
