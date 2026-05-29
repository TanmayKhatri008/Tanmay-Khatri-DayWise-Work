import json
from expense import Expense


def main():

    print("This expense tracker was created on 18th May")

    expense_file_path = "expenses.json"

    budget = 2000

    print("Running the Expense Tracker")

    while True:

        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":

                expense = get_user_expense()

                save_expense_to_file(expense, expense_file_path)

            case "2":

                summarize_expenses(expense_file_path, budget)

            case "3":

                print("\nGoodbye!")
                break

            case _:

                print("\nInvalid choice. Please try again!")


def get_user_expense():

    print("\nGetting User Expense")

    expense_name = input("Enter expense name: ")

    expense_amount = float(input("Enter the amount: "))

    expense_categories = ["Food", "Home", "Work", "Shopping", "Fun", "Misc"]

    while True:

        print("\nSelect a category:")

        for i, category_name in enumerate(expense_categories):

            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        selected_index = int(input(f"Enter the number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):

            selected_category = expense_categories[selected_index]

            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )

            return new_expense

        else:

            print("\nInvalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):

    print(f"\nSaving expense: {expense}")

    new_expense = {
        "name": expense.name,
        "category": expense.category,
        "amount": expense.amount,
    }

    try:
        with open(expense_file_path, "r") as f:

            expenses = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):

        expenses = []

    expenses.append(new_expense)

    with open(expense_file_path, "w") as f:

        json.dump(expenses, f, indent=4)

    print("\nExpense saved successfully!")


def summarize_expenses(expense_file_path, budget):

    print("\nSummarizing User Expenses")

    try:

        with open(expense_file_path, "r") as f:

            expenses_data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):

        print("\nNo expenses found!")
        return

    expenses = []

    for item in expenses_data:

        expense = Expense(
            name=item["name"], category=item["category"], amount=float(item["amount"])
        )

        expenses.append(expense)

    amount_by_category = {}

    for expense in expenses:

        key = expense.category

        if key in amount_by_category:

            amount_by_category[key] += expense.amount

        else:

            amount_by_category[key] = expense.amount

    print("\n===== Expenses By Category =====\n")

    for key, amount in amount_by_category.items():

        print(f"{key}: ${amount:.2f}")

    total_spent = 0

    for expense in expenses:

        total_spent += expense.amount

    print(f"\nTotal Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent

    print(f"Remaining Budget: ${remaining_budget:.2f}")

    if remaining_budget < 0:

        print("\nYou have exceeded your budget!")

    else:

        print("\nYou are within your budget!")


if __name__ == "__main__":

    main()
