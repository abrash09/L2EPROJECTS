
def add_expense(expenses, amount, category, description):
   # request for expense 🤭
    expense = {"amount": amount, "category": category, "description": description }
    expenses.append(expense)
    print("Expense added & saved successfully 😍\n")
    print()


# user view expenses func
def View_all_expenses (expenses):
    if not expenses:
        print("there are no expenses, Enter an expense 🥸")
    else:
        print(f"{'NO':>5} | {'ANOUNT':<15} | {'CATEGORY' :<15} | DESCRIPTION")     
        for i in range(len(expenses)):
            print(f" {i+1:<5}. | {expenses[i]['amount']:<15}: {expenses[i]['category']:<15} | {expenses[i]['description']}")
        print("-"*70)

# calculate total expense func
def calculate_total(expenses):
    if not expenses:
         print("No expenses to calculate")
    else:
        total = 0
        for cal_expense in expenses:
             total = total + cal_expense['amount']
        print(f"Total expense balance: ${total}\n")
    print()



# func for calculate_by_category
def calculate_by_category(expenses):
    if not expenses:
        print("No expenses to calculate")
    else:
        category_totals = {}
        for items in expenses:
            cat = items['category']
            amt = items['amount']
            if cat not in category_totals:
                category_totals[cat] = amt
            else:
                category_totals[cat] += amt
        for category, total in category_totals.items():
                    print(f"{category}: {total}")
        print()  

# func to delete expense
def delete_expense (expenses):
    if not expenses:
        print("No expenses to delete. 😁")
        return 
    for index, item in enumerate(expenses):
        print(f"{index +1}. {item['description']} - {item['amount']}")
    user_choice = int(input("Enter the number of the expense to delete: "))
    final_delete = (user_choice - 1)
    expenses.pop(final_delete)
    print("Expense delete successfully 😍")
