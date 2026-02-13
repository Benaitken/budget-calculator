import json

import os

DATA_FILE = "budget_data_advanced.json"

def load_data():
    """Load incomes and expenses from the JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            incomes = data.get("incomes",[])
            expenses = [tuple(e) for e in data.get("expenses",[])]
            return incomes, expenses
    return [], []

def save_data(incomes, expenses):
    with open(DATA_FILE, "w") as f:
        json.dump({"incomes": incomes, "expenses": [list(e) for e in expenses]}, f, indent=4)



def add_income(incomes):
    while True:
        try:
             amount = float(input("Enter income amount: $"))
             if amount < 0:
                 print("Income cannot be negative. Try again.")
                 continue
             incomes.append(amount)
             print(f"Income of ${amount:.2f} added!")
             break
        except ValueError:
            print("Please enter a valid number.")

def add_expense(expenses):
    while True:
        name= input("Enter expense name: ").strip()
        if not name:
            print("Expense name cannot be empty.")
            continue
        try:
            amount = float(input("Enter expense amount: $"))
            if amount < 0:
                print("Expense cannot be negative. Try again.")
                continue
            expenses.append((name, amount))
            print(f"Expense '{name}' of ${amount:.2f} added!")
            break
        except ValueError:
            print("Please enter a valid number.")   

def view_balance(income,expenses):
    total_income = sum(income)
    total_expenses = sum(amount for name, amount in expenses)
    balance = total_income -total_expenses

    print("\n Balance Summary")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${balance:.2f}\n")
 
def main():
    incomes, expenses = load_data()
    print(f"Loaded {len(incomes)} incomes and {len(expenses)} expenses.")

    while True:
        print("\n=== Budget Calculator ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. exit")

        choice = input("Choose an option:")
        if choice == "1":
            add_income(incomes)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
           view_balance(incomes, expenses)
        elif choice == "4":
            save_data(incomes, expenses)
            print("Goodbye! Your data has been saved.")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()





