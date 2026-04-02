# Task-Tracker-CLI
https://roadmap.sh/projects/task-tracker
# Task CLI

A simple command-line task manager built with Python.

## 🚀 Features

* Add tasks
* Update tasks
* Delete tasks
* Delete all tasks
* Mark tasks as in progress or done
* List all tasks or filter by status

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/M03id/Task-Tracker-CLI.git
cd task-cli
```

Install the tool:

```bash
pip install -e .
```

---

## 🧑‍💻 Usage

### Add a task

```bash
task-cli add "Buy groceries"
```

### Update a task

```bash
task-cli update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
task-cli delete 1
```

### Delete all tasks

```bash
task-cli delete-all
```

### Mark as in progress

```bash
task-cli mark 1 "in-progress"
```

### Mark as done

```bash
task-cli mark 1 "done"
```

### List all tasks

```bash
task-cli list
```

### Filter tasks

```bash
task-cli list done
task-cli list todo
task-cli list in-progress
```

---

## 🗂 Project Structure

```
task-cli/
│
├── task_cli.py
├── setup.py
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements

* Python 3.8+

---

## 📌 Notes

* Tasks are stored locally in a JSON file.
* This project is for learning purposes.

---

## 🧑‍💻 Author

Mo3id
