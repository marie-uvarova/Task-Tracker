import argparse
import tdl

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='This app can help you keep up with your chores.',
        prog='To-do list',        
    )   

    subparser = parser.add_subparsers(dest='command', help='Available commands')

    add_task = subparser.add_parser('add', help='Add a task')
    add_task.add_argument('task', metavar='TASK', help='Write the TASK')

    update_task = subparser.add_parser('update-task', help='Update the task')
    update_task.add_argument('id', metavar='ID', help='Specify the ID of the task that is being updated')
    update_task.add_argument('description', metavar='DESCRIPTION', help='Update the DESCRIPTION of the task')

    delete_task = subparser.add_parser('delete', help='Delete the task')
    delete_task.add_argument('id', metavar='ID', help='Specify the ID of the task that is being deleted')

    list_tasks = subparser.add_parser('list', help='Print tasks with a certain status (possible arguments: todo, in-progress, done; default: print all tasks)')
    list_tasks.add_argument('status', nargs='?', default='', metavar='STATUS', help='Print task with a certain STATUS (possible arguments: todo, in-progress, done; default: print all tasks)')

    update_status = subparser.add_parser('update-status', help='Update status of the task')
    update_status.add_argument('id', metavar='ID', help='Specify the ID of the task that is being updates')
    update_status.add_argument('status', metavar='STATUS', help='Update the STATUS of the task')

    args = parser.parse_args()
    todolist = tdl.ToDoList()

    if args.command == 'add':
        todolist.add(args.task)
    
    elif args.command == 'update-task':
        todolist.update(args.id, args.description)
        
    elif args.command == 'delete':
        todolist.delete(args.id)
    
    elif args.command == 'list':
        todolist.list_tasks(args.status)

    elif args.command == 'update-status':
        todolist.update_status(args.id, args.status)