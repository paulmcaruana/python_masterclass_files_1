#
#   012345678901234

parrot = "Norwegian Blue"

# slicing
print(parrot[0:6])                      # Norweg
print(parrot[3:5])                      # we
print(parrot[0:9])                      # below is the same
print(parrot[:9])
print(parrot[10:])                      # same as
print(parrot[10:14])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print(parrot[-4:-2])                    # should give us Bl
print(parrot[-4:12])

# slice with a step
print(parrot[0:6:2])                    #Nre
print(parrot[0:6:3])                    #Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]               # returns ,;: ,;
print(separators)

# just a demo for why we like the above
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])     # returns values = "".join(char if char not in separators else " " for char in number),split
print([int(val) for val in values])