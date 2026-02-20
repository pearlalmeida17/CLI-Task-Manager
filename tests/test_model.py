from taskmgr.models import tasks

# Test 1
print('=== Creating a task ===')
t = tasks(id=1, title='Test task')
print(t)
print()

# Test 2
print('=== Converting to dict ===')
d = t.to_dict()
print(d)
print()

# Test 3
print('=== Creating from dict ===')
t2 = tasks.from_dict(d)
print(t2)
print()

# Test 4
print('=== Full task with all fields ===')
t3 = tasks(id=2, title='CS Project', priority='high', tags=['uni', 'cs'], date_due='2026-02-15')
print(t3)
print(t3.to_dict())
