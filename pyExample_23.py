# For

wn = 1
print("Waiting number : {}".format(wn)) # Waiting number : 1
wn += 1
print("Waiting number : {}".format(wn)) # Waiting number : 2
wn += 1
print("Waiting number : {}".format(wn)) # Waiting number : 3
wn += 1
print("Waiting number : {}".format(wn)) # Waiting number : 4

for wn in range(4): # 4 repetitions ( variable starts at 0 when declared )
    print("Waiting number : {}".format(wn + 1))

for wn in range(1, 5): # 1 ~ 4 ( When the "in" condition is satisfied, the "for" statement code is executed. )
    print("Waiting number : {}".format(wn))


lan = ["Python", "Java", "C"]

for i in lan:
    print("I can do {}".format(i))