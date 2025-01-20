pow = lambda x,y:x**y
print(pow(2,3))

list1 = [1,2,3,4]
list2 = [5,6,7,8]
addn = map(lambda x,y: x+y, list1, list2)
print(list(addn))
