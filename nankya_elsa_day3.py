
# This script is about list and dictionary comprehensions
"""
Comprehensions (list, dictionary 
comprehensions)

"""
#List comprehensions
#Lists  are used to store multiple data in a single variable

# Example 1: Basic list compression
# Create a list of squares in range of 10
list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

# Exercise 1:
# Create a list of even numbers squares in the range of 20
even_squares = [x**2 for x in range(20) if x % 2 == 0]
print(even_squares)

#Dictionary comprehensions
#Example 2
# Create a dictionary compression for favorite cars and count the length of characters
favorite_car = ['BMW', 'Jeep', 'Mercedes', 'Fordraptor']
car_length = {car: len(car) for car in favorite_car}
print(car_length)

# Exercise 2:
# Create a list of tuple where each tuple contains number and its cube for numbers between
# 1 and 10 using a dictionary compression

cubes = {number: number**3 for number in range(1,11)}
print(list(cubes.items()))

