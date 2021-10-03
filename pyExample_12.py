# Slicing

A = "12345678-09876543"

print("First number : " + A[0]) # First number : 1 ( Index numbers start at zero. )
print("First, second, third number : " + A[0:3]) # First, second, third number : 123 ( 0:3 == 0 <= index < 3 )
print("Fourth to Seventh number : " + A[3:7]) # Fourth to Seventh number : 4567 ( 3:7 == 3 <= index < 7 )

print("First to Sixth Number : " + A[:6]) # First to Sixth Number : 123456 ( :6 == start of index <= index < 6 )
print("Nineth to End Number : " + A[9:]) # Nineth to End Number : 09876543 ( 9: == 9 <= index <= end of index )
print("The seventh number from the back to End Number : " + A[-7:]) # The seventh number from the back to End Number : 9876543