num_of_stus = int(input("Enter number of students = "))
total_marks = 0
highest_marks = -1
lowest_marks = 101
top_stu_name = ""
low_stu_name = ""
for i in range(num_of_stus):
    name = input("Enter student's name > ")
    marks = int(input("Enter student's mark = "))
    print(f"Student name: {name}")
    print(f"Student marks: {marks}")
    total_marks += marks
    if marks > highest_marks:
        highest_marks = marks
        top_stu_name = name
    if marks < lowest_marks:
        lowest_marks = marks
        low_stu_name = name
    if marks >= 80:
        print("Grade: A+")
        print("Status: Pass✅")
        print("Verdict: Excellent🌟")
    elif marks >= 70:
        print("Grade: A")
        print("Status: Pass✅")
        print("Verdict: Very Good✅")
    elif marks >= 60:
        print("Grade: B")
        print("Status: Pass✅")
        print("Verdict: Good🙂")
    elif marks >= 50:
        print("Grade: C")
        print("Status: Pass✅")
        print("Verdict: Average 😐")
    elif marks >= 40:
        print("Grade: D")
        print("Status: Pass✅")
        print("Verdict: Pass😅")
    else:
        print("Grade: F")
        print("Status: Fail❌")
avg_class_marks = total_marks/num_of_stus
print(f"Average marks of class = {avg_class_marks}")
print(f"Top student is > {top_stu_name} with marks = {highest_marks}")
print(f"Lowest student is > {low_stu_name} with marks = {lowest_marks}")