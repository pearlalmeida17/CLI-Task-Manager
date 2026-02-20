# TaskMgr - CLI Task Manager

A simple, efficient command-line task manager built with Python.

## Features

- ✅ Add tasks with priorities, due dates, and tags
- ✅ Mark tasks as complete
- ✅ Filter tasks (all/done/pending)
- ✅ Persistent JSON storage
- ✅ Clean, readable output

## Installation
```bash
git clone <CLI Task Manager>
cd taskmgr
# No dependencies needed - uses Python stdlib only!
```

## Usage

### Add a task
```bash
python -m taskmgr.cli add "Finish lab report" --priority high --due 2026-02-20 --tag uni --tag cs
```

### List tasks
```bash
python -m taskmgr.cli list              # All tasks
python -m taskmgr.cli list --done       # Completed only
python -m taskmgr.cli list --pending    # Incomplete only
```

### Mark task as done
```bash
python -m taskmgr.cli done 3
```

## Architecture

**Layered design for maintainability:**

- **models.py**: Data structures (Task class)
- **storage.py**: Persistence layer (load/save JSON)
- **service.py**: Business logic (add, complete, filter tasks)
- **cli.py**: User interface (argparse command handling)

## What I Learned

- Python dataclasses and type hints
- File I/O and JSON serialization
- Separation of concerns in software architecture
- CLI design with argparse
- Unit testing

