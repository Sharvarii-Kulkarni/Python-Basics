num1 = eval(input("Enter 1st number:"))
num2 = eval(input("Enter 2nd number:"))

print("You entered numbers: ",num1,", ",num2)
if num1 == num2:
    print("Both numbers are equal")
elif num1>num2:
    print(num1," is greater than ",num2);
else:
    print(num2, " in greater than ", num1)