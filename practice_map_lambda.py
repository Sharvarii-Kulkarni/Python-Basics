def square(n):
    return n*n
mylist = [1,2,3,4]
newlist = map(square,mylist)
print(newlist)
print(list(newlist))

x = lambda a:a*10
print(x(2))

seq = [9,4,8,2]
y = filter(lambda c:c>2,seq)
print(list(y))

z = map(lambda c:c*c,mylist)
print(list(z))