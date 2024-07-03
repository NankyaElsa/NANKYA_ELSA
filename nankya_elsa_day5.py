
#This script is about functions in python

"""
Defining functions
Function syntax and parameters
Return values
Lambda functions

Functions in python are defined using the "def" keyword, followed by
function name
paranthesis (), inside the paranthesis you put a parameter name and the colon.

"""
#Example 1:
def multiply(a, b):
    return a * b

result = multiply(5, 10)
print(result)

#Example 2:
def get_cordinates():
    return 10, 20

x,y = get_cordinates()
print(x,y)

#Exercise 1
#Define a function greet with a parameter name, set to "guest"
#and print a message, I am a software programmer

def greet(name):
    return "I am " + name + "," ,"I am a software programmer"
    

name, about = greet("Elsa")
print(name, about)

#Exercise 2
#Return multiple values of your name and age
def me():
    name = "Elsa"
    age = 17
    return name, age

name, age = me()
print(name, age)

#Notes
"""
def: keyword to define a function
function name: Name of the function
parameters: optional, arguments passed to the function
Docstrings: optional, describes the function purpose
return: optional, returns a value from the function

"""
#Syntax for defining a function
def function_name(parameters):
    """doc string"""
    #function body
    #return value

#Lambda Functions
"""
Lambda functions are small anonymous functions defined using 
the lambda keyword
The are restricted to a single expression

"""
#syntax for lambda function
#fuction_name = lambda parameter: expression

#Exampe 4: Create a lambda function to add two numbers
add = lambda a,b: a+b
print(add(45,70))

#Example 5: Use cases of lambda function for sorting
coordinates = [(1,2), (2,3), (3,1), (5,0)]
coordinates.sort(key=lambda cordinate:cordinate[1])
print(coordinates)

#Map, filter and reduce
#Example 6: Get the squares of 1 to 5 using map, filter and reduce

number_squares = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, number_squares))
print(squares)

#Exercise 3
#Define a function to get user info that accepts arbitrary
#keyword arguments and prints each key value pair
def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"user information: {key} is {value}")

# call function
get_user_info(name="Elsa", age=23, email="nankyaelsa1@gmail.com", location="Namasuba")

