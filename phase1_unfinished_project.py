#-------All in 1--------
personal_data_file = personal.txt
temp_data_file = temperature.txt
expense_data_file = expense.txt
todo_list = list.txt
student_info_file = "student_data.txt"
#first personal info & eligibility cheeker
def personal_info_eligibility_check(name,age,city,marks,personal_data_file):
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
        file.write(f"{name},{age},{city},{marks}")    
#second temperature converter
def cel_to_kel(celcius,kelvin,temp_data_file):
    celcius = int(input("Enter temperature in Celcius = "))
    kelvin = celcius+273
    print(f"{celcius} in kelvin is = {kelvin}")
    with open(temp_data_file, "a") as file:
        file.write(f"{celcius} in kelvin is = {kelvin}\n")
def cel_to_farn(celcius,farenhite,temp_data_file):
    celcius = int(input("Enter temperature in Celcius = "))
    farenhite = (celcius*9/5)+32
    print(f"{celcius} in farenhite is = {farenhite}")
    with open(temp_data_file, "a") as file:
        file.write(f"{celcius} in farenhite is = {farenhite}\n")
def faren_to_cel(celcius,farenhite,temp_data_file):
    farenhite = int(input("Enter temperature in Farenhite = "))
    celcius = (farenhite-32)*5/9
    print(f"{farenhite} in celcius is = {celcius}")
    with open(temp_data_file, "a") as file:
        file.write(f"{farenhite} in kelvin is = {celcius}\n")
def kel_to_cel(celcius,kelvin,temp_data_file):
    kelvin = int(input("Enter temperature in Kelvin = "))
    celcius = kelvin-273
    print(f"{kelvin} in celcius is {celcius}")
    with open(temp_data_file, "a") as file:
        file.write(f"{kelvin} in celcius is = {celcius}\n")
#third personal expense tracker
def personal_expense_tracker(title,amount,expense_data_file):
    title = []
    amount = []
    with open(expense_data_file, "a"):
        num = int(input("Enter number of expenses = "))
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
    with open(expense_data_file, "a"):
        file.write(f"Highest Expense: {highest_expense_title}, {highest_expense}"\n)
        file.write(f"Lowest Expense: {lowest_expense_title}, {lowest_expense}"\n)
#todo list
def todo_list(list.txt,task):
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
                with open("todo_list", "a") as file:
                    file.write(f"{i+1}.{tasks}\n")
        if choice == 2:
            for i in range(len(task)):
                print(f"Task{i+1} > {task[i]}")
        if choice == 3:
            remove_task = int(input("Enter Task Number you want to remove = "))
            task.pop(remove_task)
        if choice == 4:
            print("Exit Program.......👋")
            break
#student analyzer            
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
def average_marks(marks,num_of_stus):
    return sum(marks)/ num_of_stus
def top_stu_low_stu(marks,students):
    highest_marks = max(marks)
    lowest_marks = min(marks)
    top_stu = students[marks.index(highest_marks)]
    low_stu = students[marks.index(lowest_marks)]
    print(f"Top student is {top_stu} with score = {highest_marks}")
    print(f"Low student is {low_stu} with score = {lowest_marks}")
def input_students_data:
    student = []
    mark = []
    num_of_stus = int(input("Enter number of students = "))
    for i in range(num_of_stus):
        name = input(f"Enter Student{i+1}'s name > ")
        marks = int(input("Enter Student {i+1}'s mark = "))
        student.append(name)
        mark.append(marks)
        result = grade_system(marks)
        with open("student_info_file", "a"):
            file.write(f"Name: {name}, Marks: {marks}, Result: {result}\n")
            
        
        
        