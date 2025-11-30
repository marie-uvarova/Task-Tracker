# Task-Tracker

A simple task tracker to keep up with your chores.

# Tasks Storage

All tasks are saved to tasktracker.json. 

# Features

With this CLI app you can:

1. Add, Update, and Delete tasks

2. Mark a task as in progress or done

3. List all tasks or filter tasks by status

# How to use

Download tdl.py and todo.py. Make sure to install '''tabulate''' module.
Run by using:
'''python todo.py <command> [arguments]'''

# Commands

Add a new task
'''python todo.py add "buy cat food"'''
Update task description
'''python todo.py update-task 1 "buy groceries"'''
Delete a task
'''python todo.py delete 1'''
Update task status
'''python todo.py update-status 1 done'''
'''python todo.py update-status 1 in-progress'''
'''python todo.py update-status 1 todo'''
List all tasks
'''python todo.py list'''
List tasks by status
'''python todo.py list todo'''
'''python todo.py list in-progress'''
'''python todo.py list done'''
Help
'''python todo.py -help'''

https://roadmap.sh/projects/task-tracker


