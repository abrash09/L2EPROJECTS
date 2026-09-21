import json
# saving the saxpenses into a file func
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

# func to load expenses
def load_expenses():  
    try:
        with open ("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        return