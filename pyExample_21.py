# Changes in data structure

students = {"JongPark", "Jason", "Andrew"} # set 
print(students, type(students)) # {'JongPark', 'Jason', 'Andrew'} <class 'set'>

students = list(students) # list
print(students, type(students)) # ['JongPark', 'Jason', 'Andrew'] <class 'list'>

students = tuple(students) # tuple
print(students, type(students)) # ('JongPark', 'Jason', 'Andrew') <class 'tuple'>

students = set(students) # set
print(students, type(students)) # {'JongPark', 'Jason', 'Andrew'} <class 'set'>

age = 17 # int
print(age) # 17

age = float(age) # float
print(age) # 17.0