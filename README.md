# Task CLI

A simple command-line task manager written in Python using **only native modules** (standard library).  
Easily add, update, delete, and list tasks with JSON-based persistence — no database required.
This project is a practical task manager CLI built as part of the **[roadmap.sh Backend Developer roadmap](https://roadmap.sh/backend)** — under the *"Build a CLI Task Manager"* suggestion.


## Features

- Add new tasks
- Update task descriptions
- Change task status (`todo`, `in-progress`, `done`)
- Delete tasks by ID
- List tasks by status
- JSON persistence (`tasks.json`)

---

## Usage

### Add a task

```bash
task-cli add "Buy groceries"
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

### List all or by status

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
│   └── test_manager.py
```

## Requirements

## Running Tests


## Notes

- Data is stored in tasks.json at the root of the project.

- Task IDs are automatically incremented and managed internally.

- All logic is implemented using standard library only.