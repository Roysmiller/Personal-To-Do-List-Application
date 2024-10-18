class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False
    
    def mark_completed(self):
        self.completed = True
    
    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} [{status}] - {self.category}: {self.description}"
import json

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal, Urgent): ")
            tasks.append(Task(title, description, category))
            print("Task added!")
        
        elif choice == '2':
            if tasks:
                for idx, task in enumerate(tasks):
                    print(f"{idx + 1}. {task}")
            else:
                print("No tasks available.")
        
        elif choice == '3':
            idx = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx].mark_completed()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        
        elif choice == '4':
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                deleted_task = tasks.pop(idx)
                print(f"Deleted task: {deleted_task.title}")
            else:
                print("Invalid task number.")
        
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting application.")
            break

if __name__ == "__main__":
    main()
