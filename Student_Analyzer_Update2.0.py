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
    top_stu = student[marks.index(highest_marks)]
    low_stu = student[marks.index(lowest_marks)]
    print(f"Top student is {top_stu} with score = {highest_marks}")
    print(f"Low student is {low_stu} with score = {lowest_marks}")
student = []
marks = []
num_of_stus = int(input("Enter number of students = "))
for i in range(num_of_stus):
    name = input("Enter student name > ")
    mark = int(input(f"Enter {name}'s marks = "))
    student.append(name)
    marks.append(mark)
for i in range(num_of_stus):
    print("__________________________")
    result = grade_system(marks[i])
    name = student[i]
    print(f"Student Name: {name}")
    print(f"Result: {result}")
print("__________________________")
avg_marks = average_marks(marks,num_of_stus)
print(f"Average mark of all students = {avg_marks}")
print("__________________________")
top_stu_low_stu(marks,student)    
    