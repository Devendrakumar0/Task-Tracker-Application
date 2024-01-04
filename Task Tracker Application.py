class TaskTracker:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task_description):
        self.tasks[task_id] = task_description
        print(f'Task {task_id} added successfully.')

    def edit_task(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id] = new_description
            print(f'Task {task_id} edited successfully.')
        else:
            print(f'Task {task_id} not found.')

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f'Task {task_id} deleted successfully.')
        else:
            print(f'Task {task_id} not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for task_id, task_description in self.tasks.items():
                print(f'{task_id}: {task_description}')


def main():
    task_tracker = TaskTracker()

    while True:
        print('\nTask Tracker Menu:')
        print('1. Add Task')
        print('2. Edit Task')
        print('3. Delete Task')
        print('4. Display Tasks')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            task_id = input('Enter task ID: ')
            task_description = input('Enter task description: ')
            task_tracker.add_task(task_id, task_description)

        elif choice == '2':
            task_id = input('Enter task ID to edit: ')
            new_description = input('Enter new task description: ')
            task_tracker.edit_task(task_id, new_description)

        elif choice == '3':
            task_id = input('Enter task ID to delete: ')
            task_tracker.delete_task(task_id)

        elif choice == '4':
            task_tracker.display_tasks()

        elif choice == '5':
            print('Exiting Task Tracker. Goodbye!')
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
