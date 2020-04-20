letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]             # this prints zyxwvutsrqponmlkjihgfedcba (-1 as the stop value would not work)
print(backwards)

# create a slice that produces the characters qpo
print (letters[16:13:-1])

# slice the string to produce edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order

print(letters[:-9:-1])

# idioms
print(letters[-4:])     # wxyz
print(letters[-1:])     # z
print(letters[:1])      # a
print((letters[0]))     # a