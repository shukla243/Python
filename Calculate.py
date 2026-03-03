n1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
n2 = int(input("Enter the second number: "))

def calculate(n1,operater,n2):
    if operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    elif operator == "*":
        return n1*n2
    elif operator == "/":
        return n1/n2

if operator=='+':
    print(n1,"+",n2,"=",calculate(n1,operator,n2))

elif operator=='-':
    print(n1,"-",n2,"=",calculate(n1,operator,n2))

elif operator=='*':
    print(n1,"*",n2,"=",calculate(n1,operator,n2))

elif operator=='/':
    print(n1,"/",n2,"=",calculate(n1,operator,n2))

else:
    print("This is invalid input")
