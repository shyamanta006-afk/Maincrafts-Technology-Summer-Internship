def sum2num():                                 #sum of 2 numbers
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Sum =",a+b)

def oddEven():                             #odd even Checker
    n=int(input("Enter a number: "))
    if n%2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

def fact():                               #factorial
    n=int(input("Enter a number: "))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial =",f)

def fibonacci():
    n=int(input("Enter number of terms: "))
    a=0
    b=1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        temp=a
        a=b
        b=temp+b
def reverse():                           #revere of string
    a=input("Enter a string: ")
    print("Reversed String:",a[::-1])

def palindrome():                       #palindrome check
    a=input("Enter a string: ")
    if a == a[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

def leapyear():                        #leap year check
    a=int(input("Enter year: "))
    if (a%400 == 0) or (a%4 == 0 and a%100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def armstrong():                  #armstrong number
    n=int(input("Enter a number: "))
    power=len(str(n))
    total=sum(int(digit) ** power for digit in str(n))
    if total == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

while True:
    print("\n===== MENU =====")
    print("1. Sum of Two Numbers")
    print("2. Odd or Even Checker")
    print("3. Factorial Calculation")
    print("4. Fibonacci Sequence")
    print("5. String Reverse")
    print("6. Palindrome Check")
    print("7. Leap Year Check")
    print("8. Armstrong Number")
    print("9. Exit")
    n=int(input("Enter your choice: "))
    if n == 1:
        sum2num()
    elif n == 2:
        oddEven()
    elif n == 3:
        fact()
    elif n == 4:
        fibonacci()
    elif n == 5:
        reverse()
    elif n == 6:
        palindrome()
    elif n == 7:
        leapyear()
    elif n == 8:
        armstrong()
    elif n == 9:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")