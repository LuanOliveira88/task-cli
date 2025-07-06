# Task CLI

This project is a practical implementation of the **[Task Tracker CLI](https://roadmap.sh/projects/task-tracker)** from roadmap.sh, aimed at beginner backend developers.

A simple command-line task manager written in Python using **only native modules** (standard library).  
Easily add, update, delete, and list tasks with JSON-based persistence — no database required.


## Features

- Add new tasks
- Update task descriptions
- Change task status (`todo`, `in-progress`, `done`)
- Delete tasks by ID
- List tasks by status
- JSON persistence (`tasks.json`)

---

## Requirements

- Python 3.10 or higher
- No external dependencies — uses only Python’s standard library
- Compatible with Windows, macOS, and Linux

## Installation

**Clone the repository:**

```bash
git clone https://github.com/LuanOliveira88/task-cli.git
cd task-cli
```

## Usage

### Add a task

```bash
python main.py add "Buy groceries"
```

### Update a task description

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Mark as in-progress or done

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python main.py delete 1 
```

### List all or by status

#### List all Tasks

```bash
python main.py list  
```

#### List done tasks
```bash
python main.py list done  
```

#### List in progress tasks
```bash
python main.py list in-progress  
```

#### List todo tasks
```bash
python main.py list todo  
```

## Project Structure

```bash
task-cli/
├── main.py
├── tasks.json
├── src/
│   ├── cli.py
│   ├── database.py
│   ├── manager.py
│   ├── models.py
├── test/
│   ├── test_cli.py
│   ├── test_database.py
│   ├── test_manager.py
│   └── test_models.py
```


## Notes

- Data is stored in tasks.json at the root of the project.

- Task IDs are automatically incremented and managed internally.

- All logic is implemented using standard library only.
