import expense
import func

expenses = []

def main ():
    func.load_expenses

while True:
    print("1.  Add an expense")
    print("2.  View all expenses")
    print("3. Calculate total spending")
    print("4. Calculate spending by category")
    print("5. delete an expense")
    print("6. Exit")
    choice = input("Enter you preffered choice? ")
    if choice == "1":
        expense.add_expense(expenses)
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
    if __name__ == "_main_":
        main()
    