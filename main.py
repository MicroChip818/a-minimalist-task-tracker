import json
import sys

if len(sys.argv) < 2:
     print('Please enter a valid command')
     exit()

def save_tasks(tasks): # Saves the task dictionary into the JSON file
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

def load_tasks(): # Loads the task dictionary from the JSON file
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        save_tasks(tasks)
        with open('tasks.json', 'r') as f:
            return json.load(f)
    
def add_task(tasks, description):
    if tasks:
        task_id = max((task["id"] for task in tasks)) + 1
    else:
        task_id = 1
    tasks.append({
        'description': description,
        'status': 'todo',
        'id': task_id})
    print(f"task added | id {task_id}")
    return tasks

def update_task(tasks, task_id, new_description):
    for task in tasks:
        if task['id'] == int(task_id):
            task['description'] = new_description
            print(f"task updated | id {task_id}")
            return tasks
    print('404 | id not found')
    return tasks

def delete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == int(task_id):
            tasks.remove(task)
            print(f"task deleted | id {task_id}")
            return tasks
    print('404 | id not found')
    return tasks

def mark_in_progress(tasks, task_id):
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = 'in-progress'
            print(f"task marked in-progress | id {task_id}") 
            return tasks
    print('404 | id not found')
    return tasks

def mark_done(tasks, task_id):
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = 'done'
            print(f"task marked done | id {task_id}")
            return tasks
    print('404 | id not found')
    return tasks

def list(tasks):
    tasks = load_tasks()
    for task in tasks:
        print(f"{task['description']} | status: {task['status']} | id {task['id']}")

def list_done(tasks):
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'done':
            print(f"{task['description']} | id {task['id']}")

def list_todo(tasks):
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'todo':
            print(f"{task['description']} | id {task['id']}")

def list_in_progress(tasks):
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'in-progress':
            print(f"{task['description']} | id {task['id']}")

tasks = []

if sys.argv[1] == 'add':
    tasks = load_tasks()
    add_task(tasks, sys.argv[2])
    save_tasks(tasks)
elif sys.argv[1] == 'update':
    tasks = load_tasks()
    update_task(tasks, int(sys.argv[2]), sys.argv[3])
    save_tasks(tasks)
elif sys.argv[1] == 'delete':
    tasks = load_tasks()
    delete_task(tasks, int(sys.argv[2]))
    save_tasks(tasks)
elif sys.argv[1] == 'mark-in-progress':
    tasks = load_tasks()
    mark_in_progress(tasks, int(sys.argv[2]))
    save_tasks(tasks)
elif sys.argv[1] == 'mark-done':
    tasks = load_tasks()
    mark_done(tasks, int(sys.argv[2]))
    save_tasks(tasks)
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
    exit()
