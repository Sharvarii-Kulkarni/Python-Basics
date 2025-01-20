def maxn(n1,n2,n3):
    if n1>n2 and n1>n3:
        print("The greatest number is ",n1)
    elif n2>n1 and n2>n3:
        print("The greatest number is ",n2)
    else:
        print("the greatest number is ",n3)
n1 = eval(input("1st num: "))
n2 = eval(input("2nd num: "))
n3 = eval(input("3rd num: "))
maxn(n1,n2,n3)