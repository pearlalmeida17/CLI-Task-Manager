from taskmgr.service import add_task, mark_done, list_tasks

# Fresh empty list - NOT loading from storage!
task_list = []

t1 = add_task(task_list, "Study for exam", "high", ["uni"])
t2 = add_task(task_list, "Buy groceries", "low")
t3 = add_task(task_list, "Finish lab report", "high", ["uni", "cs"])

print("Before marking done:")
for task in task_list:
    print(f"  Task {task.id}: done={task.done}")

mark_done(task_list, t1.id)  # Use t1.id instead of hardcoded 1!

print("After marking t1 done:")
for task in task_list:
    print(f"  Task {task.id}: done={task.done}")

print(f"All: {len(list_tasks(task_list))}")
print(f"Done: {len(list_tasks(task_list, show_done=True))}")
print(f"Pending: {len(list_tasks(task_list, show_done=False))}")