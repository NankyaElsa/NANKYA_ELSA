
print("******START*****")

# This script covers the basics about python syntax and other general structures in python
#1. Commenting
#1.1 Single line comment
#Single line comments in python are done using the #(hash) sign
#1.2 Multiline comments are known as mutiline strings and they are done using three double or single quotes as shown below
"""
Hey i am a multiline comment, you can also call be a 
doc string
"""
#2.Indentation
#Python uses indentation to define the structure of code blocks (e.g., loops, conditionals, functions).
# instead of braces {} like used in other languages, indentation (usually four spaces) is used to 
# signify a block of code in python.
age = 23
if age > 5:
    # indented code block
    print("greater")
else:
    print("less")

#Variables and Data Types
#Variables in Python do not require explicit declaration. 
#The declaration happens automatically when a value is assigned to a variable. 
#Python is dynamically typed, meaning that the type is determined at runtime.
#Variable names in python can contain numbers(can not begin), letters and underscores and they are case sensistive.
x = 5        # integer
y = 3.14     # float
name = "Maggie"  # string
is_valid = True  # boolean

#Lists - Ordered, mutable collection of items, created using [], can contain items of different types.
names = ["Elsa", "Milly", "Mikey", "Willy"]
print(names)

#Tuples - Ordered, immutable collection of items.
my_tuple = (1, 2, 3, 4)
print(my_tuple)

#Sets - Unordered collection of unique items.
my_set = {1, 2, 3, 4}
print(my_set)

#Dictionaries - Collection of key-value pairs.
my_details = {"name": "Elsa", "age": 25, "course":"BSSE"}
print(my_details)

#3.Functions
#Functions in Python are defined using the def keyword, followed by the function name and parentheses.
def greeting(name):
    print(f"Hello, {name}")

greeting("Wallace")  #function call

#4.Control Flow
#Python supports various control flow statements such as if, for, and while.

#If Statement:
x = 6
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

#For Loop:
for i in range(10):
    print(i)

#While loop
while x > 0:
    print(x)
    x -= 1

#5.Exception Handling
#Exceptions in Python are handled using try, except, finally blocks.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This block is always executed")

#6.Classes and objects
#Python is an object-oriented programming language. You can define classes and create objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

person1 = Person("Arnold", 25)
person1.greet()  #call function

#7.List Comprehensions
#Python provides a concise way to create lists using list comprehensions.
squares = [x**2 for x in range(10)]
print(squares)  

#8. Modules and Packages
#Python allows you to organize your code into modules and packages. 
# A module is a file containing Python code, and a package is a collection of modules.

import add

result = add.add(5, 3)
print(result) 

print("******STOP*****")
