split_string = "This has been \nsplit over \nseveral \nlines"
print(splitString)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbedString)

print('The per shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
#or
print("""The pet shop owner said \
"No, no, 'e's uh,...he's resting". """)

another_split_string = """This string has been
split over
several
lines"""

print(anotherSplitString)

anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)

print("C:\Users\timbuchalka\notes.txt") # doesn't work because of the \
#best to use
print("C:\\Users\\timbuchalka\\notes.txt")
#but can use
print(r"C:\Users\timbuchalka\notes.txt")