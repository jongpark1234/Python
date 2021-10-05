# Continue and Break

Continuenum = [5, 7]
Breaknum = 9

for num in range(0, 11): # 0 ~ 10
    if num in Continuenum:
        print("Continue Number : {}".format(num))
        continue # Rewind without executing the sentence below.
    elif num in Breaknum:
        print("Break Number : {}".format(num))
        break # Immediately terminates the repetition statement.
    print("Normal Number : {}".format(num))

    