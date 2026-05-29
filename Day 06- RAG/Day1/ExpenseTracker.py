import json
from datetime  import datetime 


def get_input(message, data_type, validator = None, error_message = "Invalid input"):
    while True:
        try:
            value = data_type(input(message))

            if validator and not validator(value):
                print(error_message)
                continue
            return value
        except:
            print(f"Expected {data_type.__name__}, Try again")


def get_date():
      
    while True:
        date = input("Enter date in DD-MM-YYYY format, or write T for today: ").strip()
        if date == "T":
            return datetime.now().date()
        else:
            try:
                d = datetime.strptime(date, "%d-%m-%Y").date()
                return d
            except Exception:
                print("Enter correct date in correct format")


def add_expense():
    desc = input("Enter description: ")

    amount = get_input("Enter amount" , float, lambda x: x>0, "Amount must be greater than 0")
    cat = input("Enter category: ")
    date_ = get_date().strftime("%d-%m-%Y")

   
    with open("expense.json" , "r") as file:
        data = json.load(file)


    if "last_entry" not in data:
        last_entry  = 1
    else:
        last_entry = data["last_entry"] +1

    data["last_entry"] = last_entry
    

    data[str(last_entry)] = {
            "description": desc,
            "amount" : amount,
            "category" :cat,
            "date":  date_
        }
    
    

    with open("expense.json","w") as file:
        json.dump(data, file, indent = 4)
        print("Data added successfully")



def view_expense(category=None):
    ret_value = True

    with open("expense.json", "r") as file:
        data = json.load(file)

    print(f"\n{'ID':<5} {'Date':<15} {'Description':<20} {'Category':<15} {'Amount':>10}")
    print("-" * 65)

    for key in data:
        if key == "last_entry":
            continue

        if category is None or category.lower() == data[key]["category"].lower():
            ret_value = False
            print(f"{key:<5} {data[key]['date']:<15} {data[key]['description']:<20} {data[key]['category']:<15} {data[key]['amount']:>10}")

    print("-" * 65)
    return ret_value


def delete_expense(id):

    with open("expense.json" , "r") as file:
        data = json.load(file)

    exists = data.pop(id, None)

    if exists is None:
        print("The id does not exist")
        return

    else:
        print("data deleted successfully")

    with open("expense.json" , "w" ) as file:
        json.dump(data, file, indent=  4)

def monthly_summary():
    month_year = get_input(
        message="Enter month and year in MM-YYYY format: ",
        data_type=str,
        validator=lambda x: len(x) == 7 and x[2] == "-" and x[:2].isdigit() and x[3:].isdigit() and 1 <= int(x[:2]) <= 12,
        error_message="Enter in correct MM-YYYY format"
    )

    month, year = int(month_year[:2]), int(month_year[3:])

    with open("expense.json", "r") as file:
        data = json.load(file)

    total = 0
    transactions = 0
    category_breakdown = {}

    for key in data:
        if key == "last_entry":
            continue

        expense_date = datetime.strptime(data[key]["date"], "%d-%m-%Y").date()

        if expense_date.month == month and expense_date.year == year:
            amount = data[key]["amount"]
            cat = data[key]["category"]

            total += amount
            transactions += 1

            if cat not in category_breakdown:
                category_breakdown[cat] = 0
            category_breakdown[cat] += amount

    if transactions == 0:
        print(f"No expenses found for {month_year}")
        return

    print(f"\n===== Summary for {month_year} =====")
    print(f"Total Transactions : {transactions}")
    print(f"Total Spent        : {total}")
    print(f"\nCategory Breakdown:")
    for cat, amount in category_breakdown.items():
        print(f"  {cat:<20}: {amount}")

    


if __name__ == "__main__": 

    display = '''
====================== Expense Tracker ===================
1. Add Expense
2. View All Expenses
3. Filter by Category
4. Monthly Summary
5. Delete Expense
6. Exit
'''

    while True:
        
        print(display)

        choice = get_input("Enter choice: ", int, lambda x: 0<x<=6, "Enter valid choice")

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expense()

        elif choice == 3:
            cat = input("Enter category to filter: ")
            if view_expense(cat.strip()):
                print("No items in this category")

        elif choice == 4:
            monthly_summary()

        elif choice == 5:
            id = input("Enter the id you want to delete: ")
            delete_expense(id)

        elif choice == 6:
            print("Thank you for using application")
            break   