# Set

numset = {1, 2, 3, 4, 4, 4}
print(numset) # {1, 2, 3, 4}

strset1 = {"Python", "Java", "C"}
strset2 = set(["Python", "Node.js"])

# Intersection

print(strset1 & strset2) # {'Python'}
print(strset1.intersection(strset2)) # {'Python'}

# Union

print(strset1 | strset2) # {'C', 'Java', 'Node.js', 'Python'} ( Random order )
print(strset1.union(strset2)) # {'C', 'Java', 'Node.js', 'Python'} ( Random order )

# difference

print(strset1 - strset2) # {'C', 'Java'} ( Random order )
print(strset1.difference(strset2)) # {'C', 'Java'} ( Random order )

strset1.add("C#")
print(strset1) # {'Python', 'C#', 'Java', 'C'} ( Random order )
strset1.remove("C")
print(strset1) # {'Python', 'C#', 'Java'} ( Random order )

