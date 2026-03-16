
#this can be done in a module too
def add(a,b):
    sum =a+b
    return sum

def minus(a,b):
    sub =a-b
    return sub

def mul(a,b):
    into =a*b
    return into

def divide(a,b):
    
    if b==0:
        return "Not Defined"
    else:
        div=a/b
    return  div

print("--- Calculator ---\n")

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
opr=input("Enter your operation(=,-,*,/):")
if opr=="+":
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif opr=="-":
    print(f"{num1} - {num2} = {minus(num1,num2)}")
elif opr =="*":
    print(f"{num1} * {num2} = {mul(num1,num2)}")
elif opr=="/":
    print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
    print("error!!")

hi=input("")

