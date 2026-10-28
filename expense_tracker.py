
from datetime import date
import os

if not os.path.exists("expenses.txt"):
    with open("expenses.txt", "w") as file:
        file.write("Date,Category,Amount\n")

def add_expense(date, category, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{date},{category},{amount}\n")
        print("Expense added successfully!")

def read_expenses():
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
    return expenses

print(f"Expense Tracker\nOptions:\n1. Add Expense\n2. View Expenses\n")
option = input("Choose an option (1 or 2): ")
if option == "1":
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date_of_expense = date.today().strftime("%Y-%m-%d")
    add_expense(date_of_expense, category, amount)
elif option == "2":
    print(read_expenses())
else:
    print("Invalid option. Please choose 1 or 2.")

