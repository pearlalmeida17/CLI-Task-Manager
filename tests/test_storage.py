from taskmgr.storage import load_tasks, save_tasks
from taskmgr.models import tasks

print("=== Test 1: Save tasks ===")
t1 = tasks(id=1, title="Finish lab report", priority="high", tags=["uni"])
t2 = tasks(id=2, title="Buy groceries", priority="low")
t3 = tasks(id=3, title="Study for exam", priority="high", tags=["uni", "cs"])

task_list = [t1, t2, t3]
save_tasks(task_list)
print("Tasks saved!")

print()
print("=== Test 2: Load them back ===")
loaded = load_tasks()
print(f"Loaded {len(loaded)} tasks")
for t in loaded:
    print(f"  [{t.id}] {t.title} - {t.priority}")

print()
print("=== Test 3: Check they match ===")
print(f"First task title matches: {loaded[0].title == t1.title}")
print(f"Second task priority matches: {loaded[1].priority == t2.priority}")