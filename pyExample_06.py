# Operator

# Arithmetic Operator
# Arithmetic operators are binomial operators with two operands, and the direction of coupling of operands is from left to right.

# Priority : ** > / , // , % , * > + , -

print(5 + 6) # 11 ( Add )
print(5 - 6) # -1 ( Sub )
print(5 * 6) # 30 ( Mul )
print(5 / 2) # 2.5 ( Div )
print(5 ** 2) # 25 (5 ^ 2) ( Square )
print(5 % 2) # 1 ( Remainder )
print(5 // 2) # 2 ( Share )


# Comparison Operator
# Comparison operator compares the items and returns 'True' or 'False'.

print(5 > 3) # True ( The left value is greater than the right value )
print(5 < 3) # False ( The left value is less than the right value )
print(4 >= 3) # True ( The left value is greater than or equal to the right value )
print(6 <= 6) # True ( The left value is less than or equal to the right value )
print(5 == 5) # True ( The value is the same )
print(4 != 4) # False ( The value is not same )
# Reference
print(5 is 5) # True
print(5 is 5.0) # False
print(5 == 5.0) # True


# Logical Operator

# And operator returns the truth when both values are true.
print(7 > 7 and 7 == 7) # False
print(7 == 7 and 5 > 3) # True
# Or operator returns the truth even if one of the two values is true.
print(6 < 3 or 7 < 1) # False (False or False == False)
print(2 > 1 or 3 > 15) # True (True or False == True)
print(2 > 1 or 3 < 15) # True (True or True == True)
# Not operator reverses the logical value.
print(not True) # False
print(not 5 < 2) # True

