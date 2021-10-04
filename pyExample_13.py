# String Processing Function

string = 'I am JongPark'

print(string.lower()) # i am jongpark
print(string.upper()) # I AM JONGPARK
print(string[0].isupper()) # True
print(string[1].isupper()) # False
print(len(string)) # 13 ( Include a space )

# print(string.replace("JongPark", "Python")) # I am Python
# print(string.replace("am", "was")) # I was JongPark

# print(string.index("P")) # 9

# index = string.index("I")
# print(index) # 0

# index = string.index("a", index + 1)
# print(index) # 10