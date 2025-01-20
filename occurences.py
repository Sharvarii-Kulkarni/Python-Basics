#occurences of a character in string
str1="HeLlo World"

count =0
for char in str1.lower():
    if char == "l":
        count = count+1
print(count)