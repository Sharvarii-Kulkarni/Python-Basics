numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = filter(lambda x:x%2==0,numbers)
print(list(check))

square = map(lambda x:x*x, numbers)
print(list(square))

cube = map(lambda x:x*x*x, numbers)
print(list(cube))