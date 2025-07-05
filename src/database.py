import json
from typing import Optional
import os

class Database:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tasks.json'))
        if not os.path.exists(self.db_path):
            self._create_database()

    def _create_database(self):
        with open(self.db_path, 'w', encoding='utf-8') as file:
            data = {'tasks':[], 'meta':{'counter': 0, 'last_id': 0}}
            json.dump(data, file, ensure_ascii=False, indent=4)
            
    def load_tasks(self):
        with open(self.db_path, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            return tasks
        
    def save_data(self, data: list[dict]):
        tasks_dict = self.load_tasks()
        tasks_dict['tasks'] = data
        tasks_dict['meta']['counter'] = len(data)
        tasks_dict['meta']['last_id'] = max([t['id'] for t in data], default=0)
        with open(self.db_path, 'w', encoding='utf-8') as file:
            json.dump(tasks_dict, file, ensure_ascii=False, indent=4)    


    def get_next_id(self):
        data = self.load_tasks()
        return data['meta']['last_id'] + 1