import argparse

import src.manager as service

def print_task_table(tasks: list[dict]):
    if not tasks:
        print("No tasks found")
        return

    headers = ['ID', 'Description', 'Status']

    col_widths = {
        'ID': max(len(str(task['id'])) for task in tasks + [{'id': headers[0]}]),
        'Description': max(len(task['description']) for task in tasks + [{'description': headers[1]}]),
        'Status': max(len(task['status']) for task in tasks + [{'status': headers[2]}])
    }

    print(
        f"{'ID'.ljust(col_widths['ID'])} | "
        f"{'Description'.ljust(col_widths['Description'])} | "
        f"{'Status'.ljust(col_widths['Status'])}"
    )
    print('-' * (sum(col_widths.values()) + 6))  

    for task in tasks:
        print(
            f"{str(task['id']).ljust(col_widths['ID'])} | "
            f"{task['description'].ljust(col_widths['Description'])} | "
            f"{task['status'].ljust(col_widths['Status'])}"
        )
    

def main():
    parser = argparse.ArgumentParser(prog='task-cli', description='CLI Task Manager.')
    subparser = parser.add_subparsers(dest='command', required=True)

    add_parser_subcommand = subparser.add_parser('add', help='Add new Task.')
    add_parser_subcommand.add_argument('description', help='Task description.')


    update_parser_subcommand = subparser.add_parser('update', help='Update a Task by ID.')
    update_parser_subcommand.add_argument('id', type=int, help='Task ID.')
    update_parser_subcommand.add_argument('description', help='New description.')


    delete_parser_subcommand = subparser.add_parser('delete', help='Delete a Task by ID.')
    delete_parser_subcommand.add_argument('id', type=int, help='Task ID.')

    mark_in_progress_subcommand = subparser.add_parser('mark-in-progress', help='Update a Task status to in-progress.')
    mark_in_progress_subcommand.add_argument('id', type=int, help='Task ID.')

    mark_done_subcommand = subparser.add_parser('mark-done', help='Update a Task status to done.')
    mark_done_subcommand.add_argument('id', type=int, help='Task ID.')

    list_subcommand = subparser.add_parser('list', help='List Tasks.')
    list_subcommand.add_argument('status', nargs='?', help='')

    args = parser.parse_args()

    match args.command:

        case 'add':
            description = args.description
            id = service.add_task(description)
            print(f"Task added successfully (ID: {id})") 

        case 'update':
            id, description = args.id, args.description
            if service.update_task(id, description=description):
                print(f'Task {id} updated successfully')
            else:
                print(f'Task {id} not found')

        case 'delete':
            id = args.id
            if service.delete_task(id):
                print(f'Task {id} deleted succesfully.')
            else:
                print(f'Task {id} not founded.')

        case 'mark-in-progress':
            id = args.id
            if service.mark_task_in_progress(id):
                print(f'Task {id} marked as in progress')
            else:
                print(f'Task {id} not founded')

        case 'mark-done':
            id = args.id
            if service.mark_task_done(id):
                print(f'Task {id} marked as done')
            else:
                print(f'Task {id} not founded')

        case 'list':
            if args.status in (None, 'todo', 'done', 'in-progress'):
                results = service.get_tasks(args.status)
                print_task_table(results)

            else:
                print('Invalid option.')

        case _:
            print('Comando inválido')