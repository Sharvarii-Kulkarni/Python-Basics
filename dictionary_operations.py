my_dict = {'a':1,'b':'two','c':3,'d':4}
print(my_dict)

my_dict['e']=5
print("After adding: ",my_dict)

my_dict['e'] = 'five'
print("After changing: ",my_dict)

val = my_dict.pop('b')
print('value',val)
print("After deleting an element: ",my_dict)

my_dict.clear()
print("After clearing dictionary: ", my_dict)

