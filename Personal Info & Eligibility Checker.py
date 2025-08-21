name = input("Enter your name > ")
age = int(input("Enter your age > "))
city = input("Enter your city > ")
marks = int(input("Enter your marks > "))
print("Personal Info:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Marks: {marks}")
if age >= 18:
    print("You can vote ✅")
else:
    print("You can't vote ❌")
if marks >= 80:
    print("Grade: A+")
elif marks <= 79 and marks >= 70:
    print("Grade: A")
elif marks <= 69 and marks >= 60:
    print("Grade: B")
elif marks <= 59 and marks >= 50:
    print("Grade: C")
elif marks <= 49 and marks >= 40:
    print("Grade: D")
else:
     print("Grade: F")
if marks >= 40:
    print("Result: You passed ✅")
else:
    print("Result: You failed ❌")                        
    
                