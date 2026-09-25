import json
data = "expenses.json"
# saving the saxpenses into a file func
def save_expenses(expenses):
    with open(data, "w") as file:
        json.dump(expenses, file, indent=4)

# func to load expenses
def load_expenses():  
    try:
        with open (data, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return[]