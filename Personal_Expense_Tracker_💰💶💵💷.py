titles = []
amount = []
while True:
    print("1.Enter ➡️")
    print("2.Exit App")
    choice = int(input("Enter between (1-2) > "))
    if choice == 2:
        print("Exiting.....👋")
        break
    elif choice == 1:
        num_of_expenses = int(input("Enter number of expenses = "))
        print("----------------------")
        for i in range(num_of_expenses):
            expense = input("Enter expense title > ")
            cost = int(input(f"Enter amount of expenses for {expense} = "))
            titles.append(expense)
            amount.append(cost)
        def calculations(titles,amount):
            total = sum(amount)
            average = total/ len(amount)
            highest_expense = max(amount)
            highest_exp_title = titles[amount.index(highest_expense)]
            lowest_expense = min(amount)
            lowest_exp_title = titles[amount.index(lowest_expense)]
            print("----- Expense Report -----")
            print(f"Total Expenses = {total}")
            print(f"Average Expenses = {average}")
            print(f"Highest Expense = {highest_exp_title} {(highest_expense)}")
            print(f"Lowest Expense = {lowest_exp_title} {(lowest_expense)}")
            print("___________________________")
        calculations(titles,amount)
            