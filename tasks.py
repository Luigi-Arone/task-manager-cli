import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(title):
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Added task: \"{title}\"")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "x" if task["done"] else " "
        print(f"{task['id']}. [{status}] {task['title']}  ({task['created_at']})")

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print(f"Task {task_id} already done.")
                return
            task["done"] = True
            save_tasks(tasks)
            print(f"✓ Task {task_id} marked as concluded.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"✓ Task {task_id} deleted succesfully")

def clear_tasks():
    tasks = load_tasks()
    for task in tasks:
        if task["done"]:
            delete_task(task["id"])
    print("Done tasks deleted.")

def print_help():
    print(f"""
        Usage: python3 tasks.py <command> [argument]
          
        Commands:
          help          Brings up this help menu
          add <title>   Adds a new task
          list          Lists all tasks
          done <id>     Marks a task as concluded
          delete <id>   Removes a task
          clear         Deletes all concluded tasks
        
        Examples:
          python tasks.py add "Study Python"
          python tasks.py list
          python tasks.py done 1
          python tasks.py delete 2
""")
    
def main():
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: input task title")
            print('  Example: python tasks.py add "my task"')
            return
        title = " ".join(sys.argv[2:])
        add_task(title)

    elif command == "help":
        print_help()
        return

    elif command == "list":
        list_tasks()
    
    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: input task id.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: the id must be an integer.")
            return
        complete_task(task_id)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: input task id.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: the id must be an integer.")
            return
        delete_task(task_id)

    elif command == "clear":
        clear_tasks()

    else:
        print(f"Unknown command: '{command}'")
        print_help()

if __name__ == "__main__":
    main()