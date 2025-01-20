a = eval(input("Enter 1st number"))
b = eval(input("Enter 2nd number"))
print("operations are +,-,/,%,//,**")
operation = input("Enter which operation to perform:")

if operation == "+":
    print(a+b)
elif operation == "-":
    print("1st num- 2nd num",a-b)
    print("2nd num - 1st num", b-a)
elif operation == "/":
    if a>b:
        print(a/b)
    elif b>a:
        print(b/a)
    else:
        print("Div cannot be performed")
elif operation == "**":
    print("num1 raise to num2: ", a**b)
elif operation == "//":
    print(a//b)
elif operation == "%":
    print(a%b)
else:
    print("Enter valid operation")



