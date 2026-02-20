import argparse
from .service import list_tasks, add_task, mark_done
from .storage import load_tasks, save_tasks

def print_tasks(task_list):
    """
    function to display the tasks
    """
    if not task_list:
        print("No task Found!")
        return
    for t in task_list:
        box = "x" if t.done else " "
        due = t.date_due if t.date_due else "-"
        tags = ",".join(t.tags) if t.tags else "-"
        print(f"[{box}] {t.id:>3} {t.title} (due: {due}) {t.priority} tags: {tags}")

def main():
    #create parser 
    parser = argparse.ArgumentParser("tasks")
    sub = parser.add_subparsers(dest="cmd", required=True)

    #create subparser "add"
    p_add = sub.add_parser("add")
    p_add.add_argument("title")
    p_add.add_argument("--priority", default="med", choices=["low", "med", "high"])
    p_add.add_argument("--due", default=None)
    p_add.add_argument("--tag", action="append", default=[])

    #create subparser "list"
    p_list = sub.add_parser("list")
    p_list.add_argument("--done", action="store_true")
    p_list.add_argument("--pending", action="store_true")


    #create subparser "done"
    p_done = sub.add_parser("done")
    p_done.add_argument("id", type=int)

    #parsing arguments into args
    args = parser.parse_args()
    #loading the JSON file  into a list
    task_list = load_tasks()

    if args.cmd =="add":
        #for the cmd add, the task is added to the JSON file
        add_task(task_list, args.title, args.priority,args.due, args.tag) 
        save_tasks(task_list)
        print(f"Added task {args.title} command successful!")
           
    elif args.cmd == "list":
        
        #for the cmd list, the filtered list is displayed
        if args.done:
            show_done = True
        elif args.pending:
           show_done = False
        else:
           show_done = None 
        filtered = list_tasks(task_list,show_done )
        print_tasks(filtered)
        
        
    elif args.cmd == "done":
        #for the cmd done, the task with the referred task id is marked done 
        success = mark_done( task_list, args.id)
        if success:
            save_tasks(task_list)
            print(f"Marked task  {args.id} as done!")
        else:
            print(f"Task {args.id} not found! ")


if __name__=="__main__":
    main()