import expense
import func

expenses = []

def main ():
    func.load_expenses

while True:
    print("""
    =====EXPENSES TRACKER=====

    [1]. Add an expense
    [2]. View all expenses
    [3]. Calculate total spending
    [4]. Calculate spending by category
    [5]. delete an expense
    [6]. Exit""")

    choice = input("Enter you preffered choice? ")
    if choice == "1":
        amount = float(input("Enter amount "))
        category = input("Enter category ")
        description = input("Enter description ")
            
        expense.add_expense(expenses, amount, category, description)
        func.save_expenses(expenses)
        print()
    elif choice == "2":
        expense.View_all_expenses(expenses)
        print()      
    elif choice == "3":
        expense.calculate_total(expenses)
        print()
    elif choice == "4":
        expense.calculate_by_category(expenses)
        print()
    elif choice == "5":
        expense.delete_expense (expenses)
        print()
    elif choice == "6":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, please try again.\n")
    input("click enter to continue ")
    if __name__ == "_main_":
        main()
    