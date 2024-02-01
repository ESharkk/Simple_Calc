
def add(x,y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Select Option:")
print("1. Option Addition")
print("2. Option Subtraction")
print("3. Option Multiplication")
print("4. Option Division")

while True:
    choice = input("Enter desired option\n")

    if choice in ('1', '2', '3', '4'):
        try:
            num1= float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input. Please Enter a Number\n")
            continue

        if choice == "1":
            print(num1, "+ ", num2, "= ", add(num1,num2))
        elif choice == "2":
            print(num1, "1 ", num2, "= ", sub(num1,num2))
        elif choice == "3":
            print(num1, "+ ", num2, "= ", mul(num1,num2))
        elif choice == "4":
            print(num1, "+ ", num2, "= ", div(num1,num2))
        next_cal = input("Would you like to do another calculation? Yes/ No \n")
        if next_cal == ("No"):
            break
        elif next_cal == ("Yes"):
            continue
        else:
            next_cal = input("Invalid answer! Continue Yes/ No \n")
    else:
        print("Invalid Value. Please enter a number between 1 and 4")



