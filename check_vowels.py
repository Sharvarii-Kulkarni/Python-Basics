userin = input("Enter a sentence")
list1 = ['a','e','i','o','u']
count = 0
for char in userin.lower():
    if char in list1:
        count = count +1
print (count)