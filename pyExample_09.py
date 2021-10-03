# Library
# It allows us to take and use external functions, not Python's basic built-in functions.

import math # import library

print(math.ceil(300.4)) # input library name and input function.

from math import *

print(ceil(300.4)) # Simple.

print(ceil(25.3)) # 25
print(floor(25.6)) # 25
print(sqrt(625)) # 25.0

from random import * # import random library

print(randrange(100)) # Random numbers from 0 ~ 99 are returned.