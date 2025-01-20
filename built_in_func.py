str1 = "Hello this is sharvari. I am learning python."
str2 = "Hello"

rev = "".join(reversed(str2))
print(rev)

list1 = [6,5,4,3,2,'one']
list1.reverse()
print(list1)

list1.append(7)
print(list1)

list1.insert(0,'zero')
print(list1)

print(list1.count(5))
import random
random.shuffle(list1)
print(list1)

list1.sort()
print(list1)