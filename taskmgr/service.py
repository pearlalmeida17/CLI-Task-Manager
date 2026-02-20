from .models import tasks as Task
#from storage import load_tasks, save_tasks
from typing import Optional
import json


def add_task(task_list: list, title: str, priority: str = "med", tags: list[str]= None , date_due: Optional [str] = None, done:bool = False) -> Task:
   
    """
    create and  add a new taks to the task list

    args:
        task_list: existing list of tasks
        title: Task description
        priority: low, med, or igh (default: low)
        tags: Optional list of tasks
        date_due: Optional due date in YYYY-MM-DD

    Returns: 
        the newly created Task object
    """
    #Implementation
         
    #generate next available ID (default = 0 handles empty list)
    new_id = max((t.id for t in task_list), default=0 ) + 1

    #create new task object for each function call for each new task
    task = Task( id=new_id, title=title, done=False, priority=priority, tags=tags or [], date_due=date_due)

    #append the new task object to the original task list (task_list)
    task_list.append(task)

    return task
        
def mark_done(task_list: list, task_id: int)->bool:
    """
    marks a task done by ID reference
    args: 
        task_list: list of existing tasks
        task_id: ID of the task to be marked done
    
    returns:
        a boolean done; False if ID is not passed, and True if the task_id is found

    """
    #default done = False
    done = False
    for task in task_list:
        if task.id == task_id:
            task.done = True
            return True
    
    return done

def list_tasks(task_list: list, show_done: Optional[bool] = None)-> list:
    """
    Fiters tasks based on ones done and ones pending

    args:
        task_list: list of tasks 
        show_done: if True, done tasks are shown, if False pnding taks are shown; default = None
    
    Returns:
        listed_tasks: returns a filtered list of tasks
    
    """

    #empty list of tasks to stire the list of filtered tasks
    listed_tasks = []

    #no filter so, display the entire list
    if show_done is None:
        return task_list
    
    #filter to pick out done or pending tasks(as per requested) and append to the listed_list to return 
    for task in task_list:
        if task.done == show_done:
            listed_tasks.append(task)
    
    return listed_tasks
        
