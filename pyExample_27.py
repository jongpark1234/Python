# Function Example

# Write a program to find the standard weight.
# * Standard weight: Weight appropriate for each individual's height.

# ( The gender-specific formula. )
# Man : height * height * 22
# Woman : height * height * 21

# Condition 1. Calculate the standard weight within a separate function.
# Condition 2. Mark the standard weight up to the second decimal place.

# ( Output Example )
# The standard weight for a 175 cm tall man is 67.38 kg.

# ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

def std_weight(height, gender):
    if (gender == "Man" or gender == "man"):
        return round(height * height * 22, 2)
    elif (gender == "Woman" or gender == "woman"):
        return round(height * height * 21, 2)
    else:
        return "UnKnown"
    
height = 175
gender = "Woman"

print("The standard weight for a {} cm tall {} is {} kg.".format(height, gender, std_weight(height / 100, gender)))

    