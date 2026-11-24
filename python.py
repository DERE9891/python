
import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    category = input("Enter expense category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n------ EXPENSE RECORDS ------")

    for i, expense in enumerate(expenses, 1):
        print(f"\nExpense {i}")
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("Amount:", expense["amount"])


def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: {total:.2f}")


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n------ CATEGORY SUMMARY ------")

    for category, amount in summary.items():
        print(f"{category}: {amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL EXPENSE MANAGEMENT =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
