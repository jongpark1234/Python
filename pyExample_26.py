# Function

def printInfo():
    print("Hello, My name is JongPark.")
    print("I am good at Python.")
    print("I am attending Daegu Software Meister High School.")

printInfo() # Hello, My name is JongPark.
            # I am good at Python.
            # I am attending Daegu Software Meister High School.

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return round(num1 / num2, 2)

def printall(num1, num2):
    print(add(num1, num2), sub(num1, num2), mul(num1, num2), div(num1, num2))

printall(5, 13) # 18 -8 65 0.38
