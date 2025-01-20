def sum_numbers(*args):
    sum = 0
    for i in args:
        sum=sum+i
    print(sum)
sum_numbers(2,7,3)
print(type(sum))