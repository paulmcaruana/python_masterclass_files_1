age = 24
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "March", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, March, May, Jul, Aug, Oct, Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sept: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
# shows all on the same line
print()

# shows the same but all on new lines
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sept: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))
