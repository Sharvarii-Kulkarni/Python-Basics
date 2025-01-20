list1 = [1.2, 2.5, 3.8]
round_list = map(round, list1)
print(list(round_list))

list3=[1,2,4]
list2 = [1,2,4]
add = map(lambda x,y:x+y,list3,list2)
print(list(add))