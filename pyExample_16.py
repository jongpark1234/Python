# Quiz

# Ex) https://google.com
# rule 1 ) Exclude "https://" -> google.com
# rule 2 ) Excluding the after "." part that we're meeting for the first time.
# rule 3) Of the remaining letters, construct the first three digits + the number of letters + the number of 'e' in the letter + "!"


url = "https://google.com"

string = url.replace("https://", "")
string = string[:string.index(".")]

length = len(string)
countE = string.count("e")
string = string[:3]

print(string + str(length) + str(countE) + "!") # goo61!

