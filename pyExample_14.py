# Format

str1 = "I am"
str2 = "JongPark"

print(str1 + str2) # I amJongPark
print(str1, str2) # I am JongPark

print("I am %d years old." % 17) # I am 17 years old.
print("I love %s." % "Python") # I love Python.
print("I don't use '%c' word." % "F") # I don't use 'F' word.
print("I love %s and %s" % ("Apple", "Samsung")) # I love Apple and Samsung

print("I am {} years old.".format(17)) # I am 17 years old.
print("I love {} and {}.".format("Apple", "Samsung")) # I love Apple and Samsung.

print("I love {0} and {1}.".format("Apple", "Samsung")) # I love Apple and Samsung.
print("I love {1} and {0}.".format("Apple", "Samsung")) # I love Samsung and Apple.

print("I am {age} years old and I love {company}.".format(age = 17, company = "Samsung")) # I am 17 years old and I love Samsung.

age = 17
company = "Samsung"

print(f'I am {age} years old and I love {company}.') # I am 17 years old and I love Samsung.

