import time

import json
import os

commands = {
    "1": "View Expenses",
    "2": "Add Items",
    "3": "Search By Category",
    "4": "Calculate Total Expenses",
    "5": "Delete an expense",
    "6": "Clear Expense",
    "7": "Exit Program"
}

DATA_FILE = "expense.json"
box = [
   
]

def save_expense():
    with open(DATA_FILE, "w")as file:
        json.dump(box, file, indent = 4)

def load_expenses():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                    print("Invalid expense data. Starting with an empty list")
                    return []
        except (json.JSONDecodeError, OSError):
            print("Could not load expense data. Start with an empty list.")
            return []
        return []

box = load_expenses()

# This is the funtion to view  expenses
def viewing_expenses():
    if not box:
        print("No Expense has been added, Add an item to continue\n")

    else: 
        for boxes in box:
            print(f"Name: {boxes['Name']}")
            print(f"Amount: {boxes['Amount']}")
            print(f"Category: {boxes['Category']}\n")

# This is the function to add items to expense    
def add_items():
    name = input("Enter Title of Expense: ").strip()
    try:
        amount = float(input("Enter Amount spent: "))
    except TypeError:
        print("Enter Appropriate Value")
        return amount
    category = input("Specify Expense Category: ").strip()
    box.append(
        {
        "Name": name.title(),
        "Amount": amount,
        "Category": category.title()
         }

    )
    save_expense()

# This is function to find items by category
def search():
    searching = input("Enter Category to Search: ").strip().lower()
    match = []
    for boxes in box:
        if searching in boxes['Category'].lower():
            match.append(boxes)
    return match

# This is the function to calculate total expense cost
def calculating():
    total = 0
    for boxes in box:
        total += boxes['Amount']
    return total

# This is the function to delete individual expenses
def delete():
    delete_name = input("Please Enter The name of expense you want to delete: ").strip().lower()
    to_delete= []

    for boxes in box:
        if boxes['Name'].lower() == delete_name:
            to_delete.append(boxes)


    for e in to_delete:
            box.remove(e)

    if to_delete:
        save_expense()
        print(f"Deleted {len(to_delete)}\n")
    else:
        print("No Expense found with this name")

# This is the function to delete all expenses
def clear_expense():
    box.clear()
    save_expense()
    print("Expense has been cleared")

# This is the loop to make sure the program continues running until you choose the no. 7 which is close program
while True:
    try:    
        for f,s in commands.items():
            print(f"{f}: {s.title()}")

        processing_expenses = int(input("Enter a Number category to proceed: "))
        if processing_expenses == 1:
            viewing_expenses()

        elif processing_expenses == 2:
            add_items()
            print("-------Adding Expense------")
            time.sleep(3)
            print("Expense Added, You can view with the first command")
        
        elif processing_expenses == 3:
            result = search()
            if result:
                for e in result:
                    print(e)
            else:
                print("No result found")

        elif processing_expenses == 4:
            print(f"The total is #{calculating()}")

        elif processing_expenses == 5:
            delete()

        elif processing_expenses == 6:
            clear_expense()

        elif processing_expenses == 7:
            exiting = input("Are you sure you want to close this program?/nIf you " \
            "do all data would be lost\nAnswer in one word: ").strip().lower()
            if  exiting in  ("yes", "yeah", "sure", "y", "ok", "yh"):
                print(f"Ok Thanks for using this program")
                break
            else:
                print(f"{"-" * 10} Restarting Program {"-" * 10}")
                time.sleep(3)
                continue
    
    except ValueError:
        print("Enter Appropriate Values")
        print(f"{"-"*5} Restarting Program {"-"*5}")
        time.sleep(3)