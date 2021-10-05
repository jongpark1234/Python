# Standard Input, Output

print("Python", "Java", sep=", ") # Python, Java
print("Python", "Java", sep=" vs ") # Python vs Java


print("Python, Java", end=" are good\n") # Python, Java are good
print("Python, Java", end=" ")
print("are good") # Python, Java are good
# ( You can prevent automatic line breaking. )

scores = { "Python" : 100, "Java" : 80, "C" : 60 }

# ljust(), rjust()
for language, score in scores.items():
    print(language.ljust(6), score) # Secure 6 spaces and line up to the left.
# Python 100
# Java   80
# C      60

# zfill()
for num in range(1, 21): # 1 ~ 20
    print("Waiting number : " + str(num).zfill(3)) # Secure three spaces and zero the space left.
# Waiting number : 001 / 002 ㆍㆍㆍ 020


putnum = input("Press Any Value ")
print(type(putnum)) # <class 'str'>
# The data type of the value obtained by input is unconditionally str.