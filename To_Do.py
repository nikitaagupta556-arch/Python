import os
class TodoNotesBuilder:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()
    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        description = input("Enter Task Description: ").strip()
        status = input("Enter Task Status (e.g., Pending/Completed) [default: Pending]: ").strip()
        if not status:
            status = "Pending"
        with open(self.filename, 'a') as file:
            file.write(f"{task_id}|{description}|{status}\n")
        print("Task added successfully.")
    def view_tasks(self):
        if os.path.getsize(self.filename) == 0:
            print("No tasks available right now.")
            return
        print("-" * 55)
        print(f"{'ID':<10} | {'Description':<25} | {'Status'}")
        print("-" * 55)    
        with open(self.filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    task_id, description, status = parts
                    print(f"{task_id:<10} | {description:<25} | {status}")
        print("-" * 55)
    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        updated_lines = []
        found = False
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 3:
                current_id, description, status = parts
                if current_id == task_id:
                    found = True
                    print("\nWhat would you like to update?")
                    print("1. Modify Description")
                    print("2. Modify Status")
                    choice = input("Enter your choice: ").strip()
                    if choice == '1':
                        description = input("Enter new description: ").strip()
                    elif choice == '2':
                        status = input("Enter new status: ").strip()
                    else:
                        print("Invalid choice, skipping update.")
                    updated_lines.append(f"{current_id}|{description}|{status}\n")
                    print("Task updated successfully.")
                else:
                    updated_lines.append(line)
        if found:
            with open(self.filename, 'w') as file:
                file.writelines(updated_lines)
        else:
            print("Task ID not found.")
    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        updated_lines = []
        found = False
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 3:
                current_id, description, status = parts
                if current_id == task_id:
                    found = True
                    print("Task deleted successfully.")
                else:
                    updated_lines.append(line)
        if found:
            with open(self.filename, 'w') as file:
                file.writelines(updated_lines)
        else:
            print("Task ID not found.")
    def search_task(self):
        keyword = input("Enter Task ID or Keyword to search: ").strip().lower()
        found = False
        print("-" * 55)
        print(f"{'ID':<10} | {'Description':<25} | {'Status'}")
        print("-" * 55)
        with open(self.filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    task_id, description, status = parts
                    if keyword in task_id.lower() or keyword in description.lower():
                        print(f"{task_id:<10} | {description:<25} | {status}")
                        found = True             
        print("-" * 55)
        if not found:
            print("No matching tasks found.")
def main():
    filename = input("Enter the filename to store your tasks (press Enter for 'tasks.txt'): ").strip()
    if not filename:
        filename = "tasks.txt"
    app = TodoNotesBuilder(filename)
    while True:
        print("\n=== To-Do Notes Builder ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()
        print()
        if choice == '1':
            app.add_task()
        elif choice == '2':
            app.view_tasks()
        elif choice == '3':
            app.update_task()
        elif choice == '4':
            app.delete_task()
        elif choice == '5':
            app.search_task()
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()