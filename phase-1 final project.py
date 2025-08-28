#-------All in 1--------
personal_data_file = personal.txt
temp_data_file = temperature.txt
expense_data_file = expense.txt
#first personal info & eligibility cheeker
def personal_info_eligibility_check(name,age,city,marks):
    name = input("Enter your name > ")
    age = int(input("Enter your age > "))
    city = input("Enter your city > ")
    marks = int(input("Enter your marks > "))
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Marks: {marks}")
    if age >= 18:
        print("Can Vote ✅")
    else:
        print("Can't Vote❌")
    with open(personal_data_file, "a") as file:
        file.write(f"{name},{age},{city},{marks}")    
#second temperature converter
def cel_to_kel(celcius,kelvin):
    celcius = int(input("Enter temperature in Celcius = "))
    kelvin = celcius+273
    print(f"{celcius} in kelvin is = {kelvin}")
    with open(temp_data_file, "a") as file:
        file.write(f"{celcius} in kelvin is = {kelvin}\n")
def cel_to_farn(celcius,farenhite):
    celcius = int(input("Enter temperature in Celcius = "))
    farenhite = (celcius*9/5)+32
    print(f"{celcius} in farenhite is = {farenhite}")
    with open(temp_data_file, "a") as file:
        file.write(f"{celcius} in farenhite is = {farenhite}\n")
def faren_to_cel(celcius,farenhite):
    farenhite = int(input("Enter temperature in Farenhite = "))
    celcius = (farenhite-32)*5/9
    print(f"{farenhite} in celcius is = {celcius}")
    with open(temp_data_file, "a") as file:
        file.write(f"{farenhite} in kelvin is = {celcius}\n")
def kel_to_cel(celcius,kelvin):
    kelvin = int(input("Enter temperature in Kelvin = "))
    celcius = kelvin-273
    print(f"{kelvin} in celcius is {celcius}")
    with open(temp_data_file, "a") as file:
        file.write(f"{kelvin} in celcius is = {celcius}\n")
#third personal expense tracker
def personal_expense_tracker(title,amount):
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
        
        
        