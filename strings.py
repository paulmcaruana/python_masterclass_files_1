print("Today is a good day to learn Python")
print('Python is fun')
print("Python;s string are easy to use")
print('We can even include "quotes" in a string')
print("Hello" + " World")
greeting = "Hello"
name = "Paul"

#if we want a space we can add that too
print(greeting + ' ' + name)
print(greeting + name)


age = 24
print(age)

print(type(greeting))
print(type(age))
# fstrings below to allow the use of ints in a string as you see

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi= 22 / 7
print(f"Pi is approximately {pi:12.50f}")
