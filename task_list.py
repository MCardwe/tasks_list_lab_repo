tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task["description"])

def completed_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task["description"])

def task_descriptions():
    for task in tasks:
        print(task["description"])

def tasks_by_time(time):
    for task in tasks:
        if task["time_taken"] >= time:
            print(task["description"])

def task_search(search_word):
    for task in tasks:
        if search_word == task["description"]:
            print(task)

def mark_complete(name_of_task):
    for task in tasks:
        if name_of_task == task["description"]:
            task["completed"] = True

def new_task(description, completed, time_taken):
    tasks.append({"description" : description, "completed" : completed, "time_taken" : time_taken})

# print("List of completed tasks:")
# completed_tasks()

# print("List of uncompleted taks:")
# uncompleted_tasks()

# print("These are all the tasks for today:")
# task_descriptions()

# print("Tasks that take 15 mins or more")
# tasks_by_time(15)

# mark_complete("Feed Cat")

# task_search("Feed Cat")

# new_task("Go for run", True, 20)

# print(tasks)

print("Menu:")
print("1: Display All Tasks")
print("2: Display Uncompleted Tasks")
print("3: Display Completed Tasks")
print("4: Mark Task as Complete")
print("5: Get Tasks Which Take Longer Than a Given Time")
print("6: Find Task by Description")
print("7: Add a new Task to list")
print("M or m: Display this menu")
print("Q or q: Quit")

running = True

while running:
    user_selection = input("Please select an option: ")
    if user_selection == "1":
        print("These are all the tasks for today:")
        task_descriptions() 

    elif user_selection == "2":
        print("List of uncompleted taks:")
        uncompleted_tasks()

    elif user_selection == "3":
        print("List of completed tasks:")
        completed_tasks()

    elif user_selection == "4":
        mark_complete(input("Please enter the completed task: "))

    elif user_selection == "5":
        tasks_by_time(input("How much time do you have?: "))

    elif user_selection == "6":
        task_search(input("What task would you like to see?: "))

    elif user_selection == "7":
        description = input("What is the name of the task: ")
        completed_input = input("Is the task completed?: ")
        completed = False
        if completed_input.lower() == "yes":
            completed = True
        time = (int(input("How long will it takee?: ")))
        
        new_task(description, completed, time)

    elif user_selection.upper() == "M": 
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")

    elif user_selection.upper() == "QUIT" or user_selection.upper() == "Q":
        running = False
        
    else:
        print("This is an invalid option ")




