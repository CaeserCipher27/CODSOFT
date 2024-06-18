print("Welcome to Python Calculator!")
art = """ _____________________
|  _________________  |
| | KHYATI      100 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |     
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

print(art)
d = None
flag = True


def Calc():
    global d,flag
    try:
        a = float(input("Enter the First Number: "))
        b = float(input("Enter the Second Number: "))
    except ValueError:
        print("Please enter a valid number")
        Calc()
    else:
        print("Which Operation would you like to perform?")
        c = input("+ : Addition\n- : Subtraction\n* : Multiplication\n/ : Division\n")
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a / b)
        d = input("Let's perform next Calculation?\n(Yes/No):\n").lower()
        if d == 'yes':
            flag = True
            Calc()
        else:
            flag = False
            print("Thank You for using Python Calculator!")

Calc()

# while flag:
#     Calc()
#     if d == 'yes':
#         flag = True
#         Calc()
#     else:
#         flag = False
#         print("Thank You for using Python Calculator!")

# https://github.com/CaeserCipher27/CODSOFT.git
