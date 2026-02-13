def main():
    incomes = []
    expenses = []

    while True:
        print("\n=== Budget Calculator ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount:$"))
            incomes.append(amount)
            print(f"Income of $ {amount:.2f} added!")
        elif choice == "2":
           name = input("Enter expense name: ")
           amount = float(input("Enter expense amount: $"))
           expenses.append((name, amount))
           print(f"Expense '{name}' of ${amount:.2f} added!")
        elif choice == "3":
            total_income = sum(incomes)
            total_expenses = sum(amount for name, amount in expenses)
            balance = total_income -total_expenses
           
            print("\n Balance summary")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expenses: ${total_expenses:.2f}")
            print(f"Net Balance: ${balance:.2f}\n")
        elif choice == "4": 
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
   main()
