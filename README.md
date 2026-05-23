# Task Manager CLI

A simple command-line task manager built with Python. Tasks are stored locally in a JSON file.

## Features

- Add tasks
- List all tasks with status
- Mark tasks as done
- Delete tasks
- Clear all done tasks
- Persistent storage via `tasks.json`

## Requirements

- Python 3.x (no external libraries needed)

## Usage

```bash
# Brings up help
python tasks.py help

# Add a task
python tasks.py add "Study Python"

# List all tasks
python tasks.py list

# Mark task as done (use the task ID)
python tasks.py done 1

# Delete a task
python tasks.py delete 2

# Delete all done tasks
python tasks.py clear
```

## Example

```
$ python tasks.py add "Finish Boot.dev module 3"
✓ Task added: "Finish Boot.dev module 3"

$ python tasks.py add "Read chapter 5"
✓ Task added: "Read chapter 5"

$ python tasks.py list
1. [ ] Finish Boot.dev module 3  (2024-01-15 10:30)
2. [ ] Read chapter 5  (2024-01-15 10:31)

$ python tasks.py done 1
✓ Task 1 marked as done.

$ python tasks.py list
1. [x] Finish Boot.dev module 3  (2024-01-15 10:30)
2. [ ] Read chapter 5  (2024-01-15 10:31)
```

## Project Structure

```
task-manager/
├── tasks.py       # Main application
├── tasks.json     # Auto-generated when you add your first task
└── README.md
```

## What I Learned

- Reading and writing JSON files with Python
- Handling command-line arguments with `sys.argv`
- Working with lists, dictionaries, and functions
- Basic error handling
