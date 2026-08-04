import csv
import os

if not os.path.exists("expenses.csv") or os.path.getsize("expenses.csv")==0:
    f=open("expenses.csv","w",newline="")
    w=csv.writer(f)
    w.writerow(["ID","Date","Description","Amount","Category"])
    f.close()

def getid():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    next(r)
    id=1
    for i in r:
        if int(i[0])>=id:
            id=int(i[0])+1
    f.close()
    return id

def add():
    f=open("expenses.csv","a",newline="")
    w=csv.writer(f)
    id=getid()
    date=input("Enter date (YYYY-MM-DD): ")
    item=input("Enter expense name: ")

    while True:
        amnt=input("Enter amount: ")
        if amnt.isdigit():
            break
        else:
            print("Enter numeric value only.")

    while True:
        cat=input("Enter category: ")
        if cat!="":
            break
        else:
            print("Category cannot be empty.")

    w.writerow([id,date,item,amnt,cat])
    f.close()
    print("\nExpense Added.\n")

def view():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    next(r)
    print("\nExpenses:")
    empty=True
    total=0
    count=0

    for i in r:
        empty=False
        count=count+1
        total=total+int(i[3])

        print("\nID:",i[0])
        print("Date:",i[1])
        print("Expense:",i[2])
        print("Amount:",i[3])
        print("Category:",i[4])

    if empty:
        print("No expenses found.")
    else:
        print("\nTotal Expenses:",count)
        print("Grand Total:",total)

    f.close()
    print()

def srccat():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    next(r)
    src=input("Enter category to search: ")
    found=False
    total=0
    print("\nExpenses in",src,":")

    for i in r:
        if i[4].lower()==src.lower():
            found=True
            total=total+int(i[3])

            print("\nID:",i[0])
            print("Date:",i[1])
            print("Expense:",i[2])
            print("Amount:",i[3])
            print("Category:",i[4])

    if found:
        print("\nCategory Total =",total)
    else:
        print("No expense found.")

    f.close()
    print()

def montotal():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    next(r)
    month=input("Enter month (YYYY-MM): ")
    total=0
    found=False

    for i in r:
        if i[1].startswith(month):
            total=total+int(i[3])
            found=True

    if found:
        print("\nTotal spending for",month,"=",total)
    else:
        print("\nNo expenses for this month.")

    f.close()
    print()

def delete():
    f=open("expenses.csv","r")
    r=csv.reader(f)
    id=input("Enter ID to delete: ")
    data=[]
    found=False

    for i in r:
        if i[0]==id:
            found=True
        else:
            data.append(i)

    f.close()

    f=open("expenses.csv","w",newline="")
    w=csv.writer(f)
    w.writerows(data)
    f.close()

    if found:
        print("\nExpense Deleted.\n")
    else:
        print("\nID Not Found.\n")

def run():
    while True:
        print("Expense Tracker")
        print("1.Add Expense")
        print("2.View Expenses")
        print("3.Search by Category")
        print("4.View Monthly Spending")
        print("5.Delete Expense")
        print("6.Exit")
        choice=input("Enter your choice: ")

        if choice=="1":
            add()
        elif choice=="2":
            view()
        elif choice=="3":
            srccat()
        elif choice=="4":
            montotal()
        elif choice=="5":
            delete()
        elif choice=="6":
            print("Program Ended")
            break
        else:
            print("Invalid Choice\n")

run()