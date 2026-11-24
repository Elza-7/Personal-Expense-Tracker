import json
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses =[]
print("===========================")
print(" Personal Expense Tracker ")
print("===========================")
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Spending")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Search Expense")
    print("7. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        while True:
            expense_name= input("Enter your expense name: ").strip()
            if expense_name == "":
                print("Expense name cannot be empty1!")
            else:
                break
        while True:
                try:
                    amount = float(input("Enter your expense amount: "))
                    if amount <= 0:
                        print("Amount must be greater than zero!")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number!")
        while True:
            expense_category = input("Enter your expense category: ").strip()

            if expense_category == "":
                print("Category cannot be empty!")
            else:
                break
        expenses.append({
            "name":expense_name,
            "amount":amount,
            "category":expense_category
        })
        print("Expense added successfully!")
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense saved successfully!")
    elif choice ==2:
        print("\n===== YOUR EXPENSES =====")
        if not expenses:
            print("No expenses added!")
        else:
            for expense in expenses:
                print("Name: ", expense["name"])
                print("Amount: ", expense["amount"])
                print("Category: ", expense["category"])
    elif choice ==3:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print("Total spending: ₹", total)
    elif choice == 4:
        if not expenses:
            print("No expenses to delete!")
        else:
            for index, expense in enumerate(expenses):
                print(index,".",expense["name"], "-", expense["amount"])
            delete_index = int(input("Enter expense number to delete: "))

            if 0 <= delete_index < len(expenses):
                expenses.pop(delete_index)
                with open("expenses.json", "w") as file:
                    json.dump(expenses, file, indent=4)
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number!")
    elif choice ==5:
        if not expenses:
            print("No expenses to view!")
        else:
            for index, expense in enumerate(expenses):
                print(index+1,expense["name"], "-", expense["amount"])
            edit_index = int(input("Enter expense number to edit: "))-1

            if 0 <= edit_index < len(expenses):
                expense=expenses[edit_index]
                print("Selected: ", expense["name"])
                print("1. Edit name")
                print("2. Edit amount")
                print("3. Edit category")
                edit_choice = input("What do you want to edit? ")
                if edit_choice == "1":
                    new_name = input("Enter new expense name: ").strip()
                    if new_name != "":
                        expense["name"] = new_name
                        with open("expenses.json", "w") as file:
                            json.dump(expenses, file, indent=4)
                        print("Expense name updated!")
                    else:
                        print("Name cannot be empty!")
                elif edit_choice == "2":
                    while True:
                        try:
                            new_amount = float(input("Enter new expense amount: "))

                            if new_amount > 0:
                                expense["amount"] = new_amount

                                with open("expenses.json", "w") as file:
                                    json.dump(expenses, file, indent=4)

                                print("Expense amount updated!")
                                break
                            else:
                                print("Amount must be greater than zero!")
                        except ValueError:
                            print("Please enter a valid number!")
                elif edit_choice == "3":
                    new_category = input("Enter new expense category: ").strip()

                    if new_category != "":
                        expense["category"] = new_category

                        with open("expenses.json", "w") as file:
                            json.dump(expenses, file, indent=4)

                        print("Expense category updated!")
                    else:
                        print("Category cannot be empty!")
                else:
                    print("Invalid choice!")

            else:
              print("Invalid expense number!")
    elif choice == 6:
        if not expenses:
            print("No expenses available to search!")
        else:
            print("1. Search by Name")
            print("2. Search by Category")

            search_choice = input("Choose search option: ")

            found = False

            if search_choice == "1":
                search_text = input("Enter expense name: ").strip().lower()

                for expense in expenses:
                    if search_text in expense["name"].lower():
                        print("Name:", expense["name"])
                        print("Amount:", expense["amount"])
                        print("Category:", expense["category"])
                        print("--------------------")
                        found = True

            elif search_choice == "2":
                search_text = input("Enter category: ").strip().lower()

                for expense in expenses:
                    if search_text in expense["category"].lower():
                        print("Name:", expense["name"])
                        print("Amount:", expense["amount"])
                        print("Category:", expense["category"])
                        print("--------------------")
                        found = True

            else:
                print("Invalid search option!")

            if not found and search_choice in ["1", "2"]:
                print("No matching expense found!")

    elif choice == 7:
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid option!")

