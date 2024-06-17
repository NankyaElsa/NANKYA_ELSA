#This script talks about error handling in python
#Exception handling with try, except, else and finally
#Custom exceptions

"""
Notes:
Error handling in python helps to handle unexpected situations and errors.
1. Try: contains code that might throw an exception
NB: If an eception occurs, the rest of the code in the try block is skipped or ignored

2. Except: Catches and handles exceptions
NB: You can specify different handlers to different exception types

3.Else: The code runs if no exception occurs
NB: If no exception is raised in the try block, it runs

4. Finally: The code runs whether an exception is raised/ccurs or not
NB: Used for cleaning up actions

"""
#Example 1: Handle exceptions with division ny zero.
 

"""
Note:
Defining a custom Exception
class CustomError(Exception):
# Custom exception for specific error cases

def __init__(self, message):
     super().__init__(message)
     self.message = message

#Raising a custom exception
def check_value(vaue):
    if value is < 0 or value:
        raise CustomError("Value cannot be negative")
    return value

#Handle exception with try block error

"""
#Exercise 2:
#Create a custom exception InvalidAgeError and write a function that raises this exception if the given age
#is negative. Handle this custom exception when calling the function

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age =age
        self.message = f"{age} can not be negative"
        super().__init__(self.message)

def determine_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return age

try:
    age = int(input("Enter your age"))
    determine_age(age)
except InvalidAgeError:
    print("Age cannot be negative")
else:
    print(f"Age is: {age}")
finally:
    print("Execution complete")
