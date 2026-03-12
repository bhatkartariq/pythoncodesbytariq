def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Not Defined"
    return a / b


print("--- Calculator ---")

while True:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    opr = input("Enter your operation (+, -, *, /): ")

    if opr == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif opr == "-":
        print(f"{num1} - {num2} = {minus(num1, num2)}")

    elif opr == "*":
        print(f"{num1} * {num2} = {mul(num1, num2)}")

    elif opr == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    else:
        print("Error!! Invalid operation")

    choice = input("\nDo you want to continue? (y/n): ")
    if choice.lower() != "y":
        print("Calculator closed.")
        break