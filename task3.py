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
    cat=input("Enter category: ")
    date=input("Enter date (YYYY-MM-DD): ")
    w.writerow([item, amnt, cat, date])
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
        print("Category: ",i[2])
        print("Date: ",i[3])
    if empty:
        print("No expenses found.")
    f.close()
    print()

def srccat():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    src=input("Enter category to search: ")
    found=False
    print("\nExpenses in",src,":")
    for i in r:
        if i[2].lower()==src.lower():
            found=True
            print("\nExpense: ",i[0])
            print("Amount: ",i[1])
            print("Category: ",i[2])
            print("Date: ",i[3])
    if found==False:
        print("No expense found.")
    f.close()
    print()

def cattotal():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    src=input("Enter category: ")
    total=0
    found=False
    for i in r:
        if i[2].lower()==src.lower():
            total=total+int(i[1])
            found=True
    if found:
        print("\nTotal spent on",src,"= ",total)
    else:
        print("\nNo expenses found.")
    f.close()
    print()

def montotal():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    month=input("Enter month (YYYY-MM): ")
    total=0
    found=False
    for i in r:
        if i[3].startswith(month):
            total=total+int(i[1])
            found=True
    if found:
        print("\nTotal spending for",month,"= ",total)
    else:
        print("\nNo expenses for this month.")
    f.close()
    print()

while True:
    print("Expense Tracker 2.0")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Search by Category")
    print("4.View Total Expense by Category")
    print("5.View Monthly Spending")
    print("6.Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        srccat()
    elif choice=="4":
        cattotal()
    elif choice=="5":
        montotal()
    elif choice=="6":
        print("Program Ended")
        break
    else:
        print("Invalid Choice\n")