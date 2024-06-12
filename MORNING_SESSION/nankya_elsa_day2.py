"""
Control flow Structures
Conditional statements (if, elif, else)
Loops (for, while)
"""

#if, elif, else
#Exercise 1
# Calculating the discount on the prices for movies depending on age
#children under 13 years, discount for price shs 1000
#Teenagers between 13 and 18 years, discount for price she 500
# Adults 18 years and above, pay full price shs 2000
# Senior citizens 65 years above, pay shs 5000

age = int(input("How old are you"))

if age < 13:
        print("Your Discount is Shs1000")

elif age >= 13 and age < 18:
    print("Your Discount is Shs500")

elif age >=18 and age < 65:
    print("The price of the movie ticket is Shs2000")

else:
    print("The price of the movie ticket is Shs5000")

#Loops (for, while)
#Exercise 2
#Create your own list of favorite colors using for loop
colors = ["aqua", "pink", "black", "orange", "brown", "green", "blue"]
favourite_colors = []
for color in colors:
     if color[0] == "b": #my fav colors are colors starting with letter b
          favourite_colors.append(color)
print(favourite_colors)

#Ecercise 3
#Create a reverse of the input 12345 to be 54321, while loop
number = 12345
#convert number to string
string_number = str(number)
length_of_string = len(string_number)
#get the index of the last number
last_number = length_of_string - 1
reversed_string = ""
while last_number >= 0:
     reversed_string += string_number[last_number]
     last_number -= 1
print(reversed_string)
#convert string back to integer
int_reversed_string = int(reversed_string)
print(int_reversed_string) 

     



