import os 
import json

FILE = "tasks.json"

# Simple CLI for task management
def load_tasks():
    if not os.path.exists(FILE):
        return []
    try: 
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Add a new task
def add_task(text):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "text": text, "status": "todo"}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {text} | ID: {task['id']}")

# Update an existing task
def update_task(task_id, new_task):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["text"] = new_task
            save_tasks(tasks)
            print(f"Updated task ID {task_id} to: {new_task}")
            return
    print(f"Task not found.")

# Mark a task as done or todo
def mark(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            save_tasks(tasks)
            print(f"Marked task ID {task_id} as: {status}")
            return
    print(f"Task not found.")

# Delete a task by ID
def delete_task(task_id):
    tasks = load_tasks()
    if tasks[task_id]:  
        print(f"Deleted task ID {task_id}")
    else:
        print(f"Task with ID {task_id} not found.")
    tasks = [t for t in tasks if t["id"] != task_id ]
    save_tasks(tasks)
    reindex_tasks()

# Reindex tasks after deletion to maintain sequential IDs
def reindex_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        task["id"] = i + 1
    save_tasks(tasks)

# Delete all tasks
def delete_all_tasks():
    if os.path.exists(FILE):
        sure = input("Are you sure you want to delete all tasks? (y/n): ")
        if sure.lower() != "y":
            print("Deletion cancelled.")
        else:
            os.remove(FILE)
            print("All tasks deleted.")
    else:
        print("No tasks to delete.")

# List tasks with optional filtering by status
def list_tasks(filter=None):
    tasks = load_tasks()
    if tasks :
        if filter is not None:
            tasks = [t for t in tasks if t["status"] == filter]
        for task in tasks:
            print(f"{task['id']}: {task['text']} [{task['status']}]")
    else:
        print("No tasks found.")


# # ---- MAIN CLI LOGIC ----
def main():
    import sys

    args = sys.argv

    if len(args) < 2:
        print("No command provided. Use: add, update, delete, list")
        sys.exit()

    cmd = args[1]

    if cmd == "add":
        add_task(" ".join(args[2:]))

    elif cmd == "list":
        status = args[2] if len(args) > 2 else None
        list_tasks(status)

    elif cmd == "update":
        try :
            update_task(int(args[2]), " ".join(args[3:]))
        except ValueError:
            print("Invalid task. Please write a numeric ID. " \
            "Example: task update 1 New task text")

    elif cmd == "mark":
        try :
            mark(int(args[2]), args[3])
        except ValueError:
            print("Invalid task ID. Please provide a numeric ID. "\
            "Example: task mark 1 done")

    elif cmd == "delete":
        try :
            delete_task(int(args[2]))
        except ValueError:
            print("Invalid task ID. Please provide a numeric ID." \
                  "Example: task delete 1")

    else:
        print("Unknown command. Use: add, update, delete, list")


