for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i **2, i **3))
# the above allocates the spaces after the : to the number to make it look better
print()
# below changes some of the alignments so that they all line up on the left (using the < which looks like a wee arrow)
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i **2, i **3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i **2, i **3)) # the ^ centres the numbers

print()

print("Pi is approximately {0:12}".format(22/ 7))
print("Pi is approximately {0:12f}".format(22/ 7))
print("Pi is approximately {0:12.50f}".format(22/ 7))
print("Pi is approximately {0:52.50f}".format(22/ 7))
print("Pi is approximately {0:62.50f}".format(22/ 7))
print("Pi is approximately {0:<72.50f}".format(22/ 7))
print("Pi is approximately {0:<72.54f}".format(22/ 7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i **2, i **3))