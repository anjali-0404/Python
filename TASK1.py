def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                task_id, title, description, status = line.strip().split('|')
                tasks.append({
                    'task_id': int(task_id),
                    'title': title,
                    'description': description,
                    'status': status
                })
    except FileNotFoundError:
        print("No existing file found: {filename}")
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write("{task['task_id']}|{task['title']}|{task['description']}|{task['status']}\n")
    print("Tasks saved to {filename}")

def add_task(tasks, title, description):
    task_id = 1 if not tasks else max(task['task_id'] for task in tasks) + 1
    tasks.append({
        'task_id': task_id,
        'title': title,
        'description': description,
        'status': 'Pending'
    })
    print("Task added: [{task_id}] {title} - {description} - Pending")

def update_task(tasks, task_id, title=None, description=None, status=None):
    for task in tasks:
        if task['task_id'] == task_id:
            if title:
                task['title'] = title
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            print("Task updated: [{task_id}] {task['title']} - {task['description']} - {task['status']}")
            return
    print("Task with ID {task_id} not found.")

def delete_task(tasks, task_id):
    new_tasks = [task for task in tasks if task['task_id'] != task_id]
    if len(new_tasks) < len(tasks):
        print("Task with ID {task_id} deleted.")
        return new_tasks
    else:
        print("Task with ID {task_id} not found.")
        return tasks

def list_tasks(tasks):
    for task in tasks:
        print("[{task['task_id']}] {task['title']} - {task['description']} - {task['status']}")

def main():
    filename = "todo_list.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description (or leave blank): ")
            status = input("Enter new status (or leave blank): ")
            update_task(tasks, task_id, title, description, status)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            tasks = delete_task(tasks, task_id)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            break
        else:
            print("Invalid choice. Please try again.")

main()
