import csv
import os

if not os.path.exists("expenses.csv"):
    f=open("expenses.csv","w",newline="")
    f.close()

def add():
    f=open("expenses.csv","a",newline="")
    w=csv.writer(f)
    item=input("Enter expense name: ")
    amnt=input("Enter amount: ")
    w.writerow([item, amnt])
    f.close()
    print("\nExpense Added.\n")

def view():
    f=open("expenses.csv","r")
    r=csv.reader(f)

    print("\nExpenses:")
    empty=True
    for i in r:
        empty=False
        print("\nExpense: ",i[0])
        print("Amount: ",i[1])
    if empty:
        print("No expenses found.")
    f.close()
    print()

def total():
    f=open("expenses.csv","r")
    r=csv.reader(f)

    total=0
    for i in r:
        total=total+int(i[1])
    f.close()
    print("Total Expense= ",total)
    print()

while True:
    print("Expense Tracker")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.View Total Expense")
    print("4.Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        total()
    elif choice=="4":
        print("Program Ended")
        break
    else:
        print("Invalid Choice\n")