
def get_tasks_from_user():
    tasks = []
    try:
        count = int(input("How many tasks do you want to enter? "))
        for i in range(count):
            print(f"\nTask #{i + 1}:")
            name = input("Enter the task name: ")
            days_left = int(input("How many days are left until the deadline? "))
            tasks.append((name, days_left))
    except ValueError:
        print("Please enter numbers only.")
        return []
    return tasks

def sort_tasks_by_deadline(tasks):
    return sorted(tasks, key=lambda x: x[1])

def save_tasks_to_file(tasks, filename="sorted_tasks.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Your Tasks\n")
        file.write("----------\n")
        file.write("Task:               Time Left:\n")
        file.write("-------------------------------\n")
        for name, days_left in tasks:
            file.write(f"{name.ljust(20)}{str(days_left)} day(s)\n")
    print(f"\n✅ Sorted task list saved to {filename}.")

def main():
    print("📋 Task Sorting Program Based on Deadline\n")
    tasks = get_tasks_from_user()
    if tasks:
        sorted_tasks = sort_tasks_by_deadline(tasks)
        save_tasks_to_file(sorted_tasks)

if __name__ == "__main__":
    main()
