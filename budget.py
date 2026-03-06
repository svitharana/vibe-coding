def main():
    try:
        # Get total monthly budget
        total_budget = float(input("Enter your total monthly budget (LKR): "))

        # Get 3 expenses
        expenses = []
        for i in range(1, 4):
            expense = float(input(f"Enter expense {i} (LKR): "))
            expenses.append(expense)

        # Calculate sum of expenses
        total_expenses = sum(expenses)

        # Calculate remaining balance
        remaining_balance = total_budget - total_expenses

        # Display results
        print("\n--- Budget Summary ---")
        print(f"Total Budget: {total_budget:.2f} LKR")
        print(f"Total Expenses: {total_expenses:.2f} LKR")
        print(f"Remaining Balance: {remaining_balance:.2f} LKR")

        # Warning for low funds
        if remaining_balance < 500:
            print("warning:low funds")

    except ValueError:
        print("Error: Please enter valid numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
