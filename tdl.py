import json
import tabulate
from datetime import datetime as dt

def read_json():
    try:
        with open('tasktracker.json', 'r', encoding='utf-8') as tt:
            data = json.load(tt)
            return data
    except FileNotFoundError:
        with open('tasktracker.json', 'w', encoding='utf-8') as tt:
            pass

def write_json(data):
    with open('tasktracker.json', 'w', encoding='utf-8') as tt:
        json.dump(data, tt, indent=4)

class ToDoList:

    def __init__(self):        
        try:
            self.tasks = read_json()
        except json.decoder.JSONDecodeError:
            self.tasks = []
        if self.tasks is None:
            self.tasks = []

    def find_elem(self, id_n):
        if int(id_n) > len(self.tasks):
            raise ValueError('Task not found.')
        else:
            elem = self.tasks[int(id_n) - 1]
        return elem

    def add(self, task_text):        
        id_n = len(self.tasks) + 1
        task = {
            'description': task_text,
            'status': 'todo',
            'createdAT': dt.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAT': dt.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
        self.tasks.append({id_n: task})
        write_json(self.tasks)

        print(f'Task added successfully (ID: {id_n})')

    def update(self, id_n, task):
        if int(id_n) > len(self.tasks) or int(id_n) <= 0:
            raise ValueError('Task not found.')
        else:
            elem = self.tasks[int(id_n) - 1]
            elem[f'{id_n}']['description'] = task
            elem[f'{id_n}']['updatedAT'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')
            write_json(self.tasks)

        print(f'Task {id_n} updated successfully')

    def delete(self, id_n):
        if int(id_n) > len(self.tasks) or int(id_n) <= 0:
            raise ValueError('Task not found.')
        else:
            for i in range(len(self.tasks) - 1):
                if i + 1 >= int(id_n):
                    self.tasks[i][f'{i + 1}'] = self.tasks[i + 1][f'{i + 2}']
            write_json(self.tasks[:len(self.tasks)-1])

        print(f'Task {id_n} deleted successfully')

    def list_tasks(self, status=''):
        data = read_json()
        A = []
        new_dict = {}
        for i in range(len(data)):
            if data[i][f'{i + 1}']['status'] == status:
                new_dict = {'id': i + 1, **data[i][f'{i + 1}']}
                A.append(new_dict)
            elif status == '':
                new_dict = {'id': i + 1, **data[i][f'{i + 1}']}
                A.append(new_dict)
        if A == []:
            print('No tasks found')
        else:
            print(tabulate.tabulate(A, headers="keys"))

    def update_status(self, id_n, status):
        elem = ToDoList.find_elem(self, id_n)
        elem[f'{id_n}']['status'] = status
        elem[f'{id_n}']['updatedAT'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        write_json(self.tasks)

        print(f'Task {id_n} status updated successfully') 