# Dictionary

dv = {
    1 : "Python",
    2 : "C",
    3 : "Node.js",
    100 : "JongPark"
}

print(dv) # {1: 'Python', 2: 'C', 3: 'Node.js', 100: 'JongPark'}

print(dv[1]) # Python
print(dv[1], dv[2], dv[3]) # Python C Node.js
print(dv[100]) # JongPark

print(3 in dv) # True
print(5 in dv) # False

strdv = {
    "First" : "JongPark",
    "Second" : "Python"
}

print(strdv) # {'First': 'JongPark', 'Second': 'Python'}

print(strdv["First"]) # JongPark
print(strdv["Second"]) # Python

strdv["Third"] = "Node.js"

print(strdv) # {'First': 'JongPark', 'Second': 'Python', 'Third': 'Node.js'}
print(strdv["Third"]) # Node.js

del strdv["Third"]
print(strdv) # {'First': 'JongPark', 'Second': 'Python'}

print(strdv.keys()) # dict_keys(['First', 'Second'])
print(strdv.values()) # dict_values(['JongPark', 'Python'])
print(strdv.items()) # dict_items([('First', 'JongPark'), ('Second', 'Python')])

strdv.clear()
print(strdv) # {}
