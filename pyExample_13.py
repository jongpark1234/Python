# String Processing Function

string = 'I am JongPark'

print(string.lower()) # i am jongpark
print(string.upper()) # I AM JONGPARK
print(string[0].isupper()) # True
print(string[1].isupper()) # False
print(len(string)) # 13 ( Include a space )

print(string.count("a")) # 2
print(string.count("I")) # 1

print(string.replace("JongPark", "Python")) # I am Python
print(string.replace("am", "was")) # I was JongPark

print(string.index("P")) # 9
print(string.index("I")) # 0

print(string.find("JongPark")) # 5
print(string.find("am")) # 2


