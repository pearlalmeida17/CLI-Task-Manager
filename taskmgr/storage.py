from .models import tasks
import json
from pathlib import Path

def load_tasks() -> list[tasks]:
    
    """
    load tasks from the JSON file into a list 

    if the file doesn't exists, it creates it
    converts the JSON file raw data into dictionaries
    converts each dictionaries into task objects using from_dict() fucntion 
    appends the objects into a task_list 

    return:
        task_list with the task objets

    """
    
    data_path = Path("data/tasks.json")
    
    if not data_path.exists():
        data_path.parent.mkdir(parents=True,exist_ok=True)
        data_path.write_text("[]")
        return []

    if data_path.exists():
        raw_json = data_path.read_text()
        task_dicts = json.loads(raw_json)
        
        task_list = []
        for task_dict in task_dicts:
            task_obj = tasks.from_dict(task_dict)
            task_list.append(task_obj)
        return task_list        

def save_tasks(tasks: list[tasks]) -> None:

    """
    writes the tasks list into JSON file
    if the file doesn't exists, it creates it
    converts the tasks object (a list) into a dictionary using the function to_dict()
    the dictionary list is converted into a string using string 
    te string is written into the file 
    
    """
    
    data_path = Path("data/tasks.json")
    
    
    data_path.parent.mkdir(parents=True, exist_ok=True)
    dict_list = []
    for task in tasks:
        dict_list.append(task.to_dict())
        
    json_string = json.dumps(dict_list)
    data_path.write_text(json_string)
        