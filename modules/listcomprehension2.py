cube = [x**3 for x in range(1,31) if x%2!=0]
print(cube)

strlist = [str(x) for x in range(1,16) if x%3==0]
print(strlist)

tup = [(x,x**2) for x in range(1,11)]
print(tup)

combinations = [a+b for a in "ABC" for b in "ABC"]
print(combinations)