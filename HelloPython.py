x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

x = y = z = "Orange"
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = "inutuitive"

def myfunc():
  print("Python is " + x)

myfunc()

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

import random

print(random.randrange(1, 10))

#Single-line comments look like this
"""and multi-line comments look like this
similarily, multi-line string literals can be declared like this:"""
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)