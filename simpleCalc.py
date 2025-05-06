n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))

operator=input("Enter operation: ")

if operator == '+':
    print(n1+n2)
elif operator == '-':
    print(n1-n2)
elif operator == '*':
    print(n1*n2)
elif operator == '/':
    if n2 != 0:
        print(n1/n2)
    else:
        print("Invalid input")
