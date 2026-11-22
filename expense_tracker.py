
import csv
from datetime import datetime

expenses = []

def add_expense():

    print("\n--- Add Expense ---")


    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Please enter a valid date.")

    
    while True:
        category = input("Enter category: ").strip()

        if category:
            break
        else:
            print("Category cannot be empty!")


    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    
    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")



def show_totals():

    print("\n--- Spending by Category ---")

    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    for category, total in totals.items():
        print(category, ":", total)



def save_to_csv():

    with open("expenses.csv", "w", newline="") as file:

        fieldnames = ["date", "category", "amount"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("\nExpenses saved to expenses.csv")

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Category Totals")
    print("3. Save Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_totals()

    elif choice == "3":
        save_to_csv()

    elif choice == "4":
        save_to_csv()
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
