a=int(input("Enter a number:"))
c=input("Enter an operator (+, -, *, /): ")
b=int(input("Enter another number:"))
if c == '+':
    print("Addition:", a + b)
elif c == '-':
    print("Subtraction:", a - b)
elif c == '*':
    print("Multiplication:", a * b)
elif c == '/':
    print("Division:", a / b)