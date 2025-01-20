def multiply(a,  *args):
    prod=a
    for i in args:
        prod=prod*i
    print(prod)
multiply(2,4,6,5)