# A Minimalist Task Tracker
## About
A Minimalistic Task Tracker (AMTT) is a CLI-based task tracker that stores tasks in a JSON file using various commands.

## Important
Project URL: https://roadmap.sh/projects/task-tracker

To run this project, you must install Python if it is not on your computer already: https://www.python.org/downloads/

## How to run this project

### With Git
1A. Clone the repository:
```bash
git clone https://github.com/MicroChip818/a-minimalist-task-tracker.git
cd a-minimalist-task-tracker
```

### Without Git
1B. Download the ZIP folder and extract it.

### Next Steps
2. Create and activate a virtual environment:
```bash
# On Linux or MacOS:
python3 -m venv .venv
source .venv/bin/activate
# On Windows:
python -m venv .venv
.venv\Scripts\activate
```
3. Install the package:
```bash
pip install -e .
```

Once you are finished with these steps, you can run commands through any terminal.

## Commands
There are 6 commands as of creating this project.

All commands start with ```task-cli```. Please add quotation marks around task NAMES to avoid formatting/argument errors.

1. ```add [task-name]``` Adds a task with a custom name. New tasks have a status of ```todo```
2. ```update [task-id] [new-task-name]``` Updates a task's name
3. ```delete [task-id]``` Deletes a task with a certain ID
4. ```mark-in-progress [task-id]``` Marks a task as ```in-progress``` status
5. ```mark-done [task-id]``` Marks a task ```done``` status
6. ```list-[status]``` Prints every task with a certain status in order of ID. You can also omit ```-[status]``` to print the full list of tasks.

## How to access your tasks
After cloning the project and adding your first task, a tasks.json file will be created. You can open this file in any text editor.