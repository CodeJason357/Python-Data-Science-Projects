# ==============================
# Menu-Driven Student Analyzer
# ==============================

# ---------- Functions ----------
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

def read_student_data(data_file):
    students = []
    marks = []
    try:
        with open(data_file, "r") as file:
            for line in file:
                name, mark = line.strip().split(",")
                students.append(name)
                marks.append(int(mark))
        print("Old student data loaded.\n")
    except FileNotFoundError:
        print("No old student data found. New file will be created.\n")
    return students, marks

def add_new_students(students, marks, data_file):
    num_of_stus = int(input("Enter number of new students = "))
    for i in range(num_of_stus):
        name = input(f"Enter student {i+1} name > ")
        mark = int(input(f"Enter {name}'s marks = "))
        students.append(name)
        marks.append(mark)
        with open(data_file, "a") as file:
            file.write(f"{name},{mark}\n")
    print("\nNew students added successfully!\n")

def show_results(students, marks, result_file):
    with open(result_file, "w") as file:
        file.write("Student Analyzer Results\n")
        file.write("__________________________\n")
        for i in range(len(students)):
            result = grade_system(marks[i])
            name = students[i]
            print("__________________________")
            print(f"Student Name: {name}")
            print(f"Result: {result}")
            file.write(f"Student Name: {name}\n")
            file.write(f"Result: {result}\n")
            file.write("__________________________\n")

        avg_marks = average_marks(marks, len(students))
        print("__________________________")
        print(f"Average mark of all students = {avg_marks}")
        print("__________________________")
        top_stu_low_stu(marks, students)
        file.write(f"Average mark of all students = {avg_marks}\n")
        file.write(f"Top student is {students[marks.index(max(marks))]} with score = {max(marks)}\n")
        file.write(f"Low student is {students[marks.index(min(marks))]} with score = {min(marks)}\n")
    print(f"\nResults saved to {result_file}!\n")

# ---------- Main Program ----------
data_file = "students.txt"
result_file = "results.txt"

students, marks = read_student_data(data_file)

while True:
    print("====== Student Analyzer Menu ======")
    print("1. Show all student results")
    print("2. Add new students")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3) > ")

    if choice == "1":
        if len(students) == 0:
            print("No student data available. Add students first.\n")
        else:
            show_results(students, marks, result_file)
    elif choice == "2":
        add_new_students(students, marks, data_file)
    elif choice == "3":
        print("Exiting program... Bye! 👋")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.\n")