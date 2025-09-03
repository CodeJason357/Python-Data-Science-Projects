#-------All in 1--------
def personal_info_eligibility_check(personal_data_file):
    info = []
    name = input("Enter your name > ")
    info.append(name)
    age = int(input("Enter your age > "))
    info.append(age)
    city = input("Enter your city > ")
    info.append(city)
    marks = int(input("Enter your marks > "))
    info.append(marks)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Marks: {marks}")
    if age >= 18:
        print("Can Vote ✅")
    else:
        print("Can't Vote❌")
    print(info)
    with open(personal_data_file, "a") as file:
        file.write(f"{name},{age},{city},{marks}\n")


# second temperature converter
def cel_to_kel(temp_data_file):
    celcius = int(input("Enter temperature in Celcius = "))
    kelvin = celcius + 273
    print(f"{celcius} in kelvin is = {kelvin}")
    with open(temp_data_file, "a") as file:
        file.write(f"{celcius} in kelvin is = {kelvin}\n")


def cel_to_farn(temp_data_file):
    celcius = int(input("Enter temperature in Celcius = "))
    farenhite = (celcius * 9 / 5) + 32
    print(f"{celcius} in farenhite is = {farenhite}")
    with open(temp_data_file, "a") as file:
        file.write(f"{celcius} in farenhite is = {farenhite}\n")


def faren_to_cel(temp_data_file):
    farenhite = int(input("Enter temperature in Farenhite = "))
    celcius = (farenhite - 32) * 5 / 9
    print(f"{farenhite} in celcius is = {celcius}")
    with open(temp_data_file, "a") as file:
        file.write(f"{farenhite} in celcius is = {celcius}\n")


def kel_to_cel(temp_data_file):
    kelvin = int(input("Enter temperature in Kelvin = "))
    celcius = kelvin - 273
    print(f"{kelvin} in celcius is {celcius}")
    with open(temp_data_file, "a") as file:
        file.write(f"{kelvin} in celcius is = {celcius}\n")


# third personal expense tracker
def personal_expense_tracker(expense_data_file):
    title = []
    amount = []
    num = int(input("Enter number of expenses = "))
    with open(expense_data_file, "a") as file:
        for i in range(num):
            name = input("Enter title >")
            money = int(input("Enter amount = "))
            title.append(name)
            amount.append(money)
            file.write(f"Expense Title: {name}\n")
            file.write(f"Expense Amount: {money}\n")
        highest_expense = max(amount)
        lowest_expense = min(amount)
        highest_expense_title = title[amount.index(highest_expense)]
        lowest_expense_title = title[amount.index(lowest_expense)]
        file.write(f"Highest Expense: {highest_expense_title}, {highest_expense}\n")
        file.write(f"Lowest Expense: {lowest_expense_title}, {lowest_expense}\n")


# todo list
def todo_list_func(todo_file):
    task = []
    while True:
        print("1.Add New Task")
        print("2.Show Task List")
        print("3.Mark Task as Done/Remove Task")
        print("4.Exit")
        choice = int(input("Enter choice between (1-4) >"))
        if choice == 1:
            num_of_tasks = int(input("Enter number of tasks you want to add = "))
            for i in range(num_of_tasks):
                tasks = input(f"Enter Task{i+1} = ")
                task.append(tasks)
                with open(todo_file, "a") as file:
                    file.write(f"{i+1}.{tasks}\n")
        elif choice == 2:
            for i in range(len(task)):
                print(f"Task{i+1} > {task[i]}")
        elif choice == 3:
            remove_task = int(input("Enter Task Number you want to remove = ")) - 1
            if 0 <= remove_task < len(task):
                task.pop(remove_task)
            else:
                print("Invalid task number.")
        elif choice == 4:
            print("Exit Program.......👋")
            break


# student analyzer
def grade_system(marks):
    if marks >= 80:
        return "Grade: A+ | Status: Pass✅ | Verdict: Excellent🌟"
    elif marks >= 70:
        return "Grade: A | Status: Pass✅ | Verdict: Very Good✅"
    elif marks >= 60:
        return "Grade: B | Status: Pass✅ | Verdict: Good🙂"
    elif marks >= 50:
        return "Grade: C | Status: Pass✅ | Verdict: Average 😐"
    elif marks >= 40:
        return "Grade: D | Status: Pass✅ | Verdict: Pass😅"
    else:
        return "Grade: F | Status: Fail❌"


def average_marks(mark, num_of_stus):
    return sum(mark) / num_of_stus


def top_stu_low_stu(mark, student):
    highest_marks = max(mark)
    lowest_marks = min(mark)
    top_stu = student[mark.index(highest_marks)]
    low_stu = student[mark.index(lowest_marks)]
    print(f"Top student is {top_stu} with score = {highest_marks}")
    print(f"Low student is {low_stu} with score = {lowest_marks}")


def input_students_data(student_info_file):
    student = []
    mark = []
    Result = []
    num_of_stus = int(input("Enter number of students = "))
    with open(student_info_file, "a") as file:
        for i in range(num_of_stus):
            name = input(f"Enter Student{i+1}'s name > ")
            marks = int(input(f"Enter Student {i+1}'s mark = "))
            student.append(name)
            mark.append(marks)
            result = grade_system(marks)
            Result.append(result)
            average = average_marks(mark, num_of_stus)
            top_stu_low_stu(mark, student)
            print(f"Name: {student[i]}, Marks: {mark[i]}, Result: {Result[i]}")
            file.write(f"Name: {name}, Marks: {marks}, Result: {result}\n")


# File Paths
personal_data_file = "personal.txt"
temp_data_file = "temperature.txt"
expense_data_file = "expense.txt"
todo_file = "list.txt"
student_info_file = "student_data.txt"

# ------- MAIN MENU --------
while True:
    print("1. Personal Info & Elegibility Checker 📈")
    print("2. Temperature Converter 🌡️")
    print("3. Peraonal Expense Tracker 💷💵💶💰")
    print("4. Todo List 📊")
    print("5. Student Result Analyzer 📊")
    print("6. Exit")
    Choice = int(input("Enter Choice Between (1-6) > "))
    if Choice == 1:
        personal_info_eligibility_check(personal_data_file)
    elif Choice == 2:
        print("1. Celcius -> Kelvin")
        print("2. Celcius -> Farenhite")
        print("3. Farenhite -> Celcius")
        print("4. Kelvin -> Celcius")
        temp_choice = int(input("Enter choice between (1-4) > "))
        if temp_choice == 1:
            cel_to_kel(temp_data_file)
        elif temp_choice == 2:
            cel_to_farn(temp_data_file)
        elif temp_choice == 3:
            faren_to_cel(temp_data_file)
        elif temp_choice == 4:
            kel_to_cel(temp_data_file)
    elif Choice == 3:
        personal_expense_tracker(expense_data_file)
    elif Choice == 4:
        todo_list_func(todo_file)
    elif Choice == 5:
        input_students_data(student_info_file)
    elif Choice == 6:
        print("Exiting Program....👋")
        break