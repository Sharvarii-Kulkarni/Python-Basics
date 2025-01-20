def print_details(**kwargs):
    print(type(kwargs))
    for key,val in kwargs.items():
        print(key," : ",val)

print_details(a=4,fruit="apple")