# List

num1 = 10
num2 = 20
num3 = 30

print(num1, num2, num3) # 10 20 30

numlist = [10, 20, 30] # Proclaim List. ( Type : List[int] )

print(numlist) # [10, 20, 30]
print(numlist[0], numlist[1], numlist[2]) # 10 20 30 ( index number start at 0 )

numlist = [7, 3, 5, 8, 2, 4, 7, 1, 4, 8, 0, 21]
numlist.sort()
print(numlist) # [0, 1, 2, 3, 4, 4, 5, 7, 7, 8, 8, 21]

numlist.reverse()
print(numlist) # [21, 8, 8, 7, 7, 5, 4, 4, 3, 2, 1, 0]

numlist.clear()
print(numlist) # []

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

namelist = ["JongPark", "Python", "Java Script"] # Proclaim List. ( Type : List[str] )

print(namelist) # ['JongPark', 'Python', 'Java']
print(namelist[0], namelist[1], namelist[2]) # JongPark Python Java Script
print("My name is", namelist[0] + ". I can do", namelist[1], "and", namelist[2]) # My name is JongPark. I can do Python and Java Script

print(namelist.index("JongPark")) # 0
print(namelist.index("Java Script")) # 2

namelist.append("C")

print(namelist[3]) # C

print("My name is", namelist[0] + ". I can do", namelist[1] + ",", namelist[2], "and", namelist[3]) # My name is JongPark. I can do Python, Java Script and C

namelist.insert(2, "Java") # namelist[2] == "Java", namelist[3] == "Java Script"

print("My name is", namelist[0] + ". I can do", namelist[1] + ",", namelist[2] + ",", namelist[3], "and", namelist[4]) # My name is JongPark. I can do Python, Java, Java Script and C

namelist.pop()

print(namelist) # ['JongPark', 'Python', 'Java', 'Java Script']

namelist.pop()
namelist.pop()

print(namelist) # ['JongPark', 'Python']

namelist.append("Python")

print(namelist.count("Python")) # 2
print(namelist.count("JongPark")) # 1

# ㅡㅡㅡㅡ

mixlist = ["JongPark", 17, True]
numlist = [1, 2, 3, 5, 4]

numlist.extend(mixlist)
print(numlist) # [1, 2, 3, 5, 4, 'JongPark', 17, True]












