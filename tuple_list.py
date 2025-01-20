employee_data = ('John', 'Doe', 34, 'Developer', 'New York')

def f(*args):
    for items in args:
        return items

print(f(employee_data))

def unpackdata(data):
    name,surname,age,job,address=data
    return name,surname,age,job,address

name,surname,age,job,address=unpackdata(employee_data)
print(name)
print(age)

if 'Developer' in employee_data:
    print("yes it is present")
else:
    print("Not present")

newlist = list(employee_data)
print(newlist)
print(type(newlist))
newlist.append('Full-time')
print(newlist)