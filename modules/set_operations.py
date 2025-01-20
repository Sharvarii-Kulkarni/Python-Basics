skills_A = {'Python', 'Java', 'SQL'}
skills_B = {'Python', 'HTML', 'CSS'}

print(skills_A.intersection(skills_B))
print(skills_A.difference(skills_B))
print(skills_A.union(skills_B))

numbers = [1, 2, 2, 3, 4, 4, 5]
set1=set(numbers)
print(set1)
numbers2 = list(set1)
print(numbers2)