# While

import random

num = 0

while (num < 5): # if num is loss than 5
    print(num) # print num
    num += 1 # num = num + 1
# total 5 times repetition

numlist = list(range(1, 101)) # 1 ~ 100 list.

while (num != 50): # Repeat until you get 50.
    num = random.sample(numlist, 1)[0]
    print(num)