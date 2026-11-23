import json
expenses =[]
print("===========================")
print(" Personal Expense Tracker ")
print("===========================")
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Spending")
    print("4. Exit")
    print("5. Delete Expense")
    choice = int(input("Choose an option: "))
    if choice == 1:
        expense_name= input("Enter your expense name: ")
        amount = float(input("Enter your expense amount: "))
        expense_category = input("Enter your expense category: ")
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
        print("Thank you for using Expense Tracker!")
        break
    elif choice == 5:
        if not expenses:
            print("No expenses to delete!")
        else:
            for index, expense in enumerate(expenses):

                print(index,".",expense["name"], "-", expense["amount"])

            delete_index = int(input("Enter expense number to delete: "))

            if 0 <= delete_index < len(expenses):
                expenses.pop(delete_index)
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number!")
    else:
        print("Invalid option!")

