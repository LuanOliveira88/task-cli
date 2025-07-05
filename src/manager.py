from src.models import Task
from src.database import Database


db = Database()

def add_task(description: str):
    task = Task(id=db.get_next_id(), description=description)
    tasks_data = db.load_tasks()
    tasks_data['tasks'].append(task.to_dict())
    db.save_data(tasks_data['tasks'])
    return task.id

def update_task(id: int, **kwargs):
    tasks_dict = db.load_tasks()

    updated = False
    for task in tasks_dict['tasks']:
        if task['id'] == id:
            for key, value in kwargs.items():
                if key in task:
                    task[key] = value
            updated = True
            break

    if updated:           
        db.save_data(data=tasks_dict['tasks'])
    return updated


def delete_task(id: int):
    tasks_dict = db.load_tasks()
    data = tasks_dict['tasks']
    for index, task in enumerate(data):
        if task['id'] == id:
            del data[index]
            db.save_data(data)
            return True
    return False

def mark_task_done(id: int):
    return update_task(id=id, status='done')

def mark_task_in_progress(id: int):
    return update_task(id=id, status='in-progress')

def get_tasks(status=None):
    tasks_dict = db.load_tasks()
    data = tasks_dict['tasks']
    
    result = data if status is None else list(filter(lambda t: t['status'] == status, data))
    
    return list(result)

def list_tasks(status=None):
    result = get_tasks(status)
