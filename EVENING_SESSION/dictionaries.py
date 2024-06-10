
"""
Exercise5 (Dictionaries)

"""
#1.	With reference to the dictionary below, write a python program to print the value of the shoe size. 
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(shoes["size"])

#2.	Write a python program to change the value “Nick” to “Adidas”
shoes["brand"] = "Adidas"
print(shoes)

#3.	Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
shoes["type"] = "sneakers"
print(shoes)

#4.	Write a python program to return a list of all the keys in the dictionary above.
all_keys = shoes.keys()
print(all_keys)

#5.	Write a python program to return a list of all the values in the dictionary above.
all_values = shoes.values()
print(all_values)

#6.	Check if the key “size” exists in the dictionary above.
if "size" in shoes:
    print("Key size is in the dictionary")
else:
    print("key size is not in the dictionary")
    
#7.	Write a python program to loop through the dictionary above.
for key, value in shoes.items():
    print(f"{key} : {value}")
    
#8.	Write a python program to remove “color” from the dictionary.
shoes.pop("color")
print(shoes)

#9.	Write a python program to empty the dictionary above.
empty = shoes.clear()
print(empty)

#10.Write a dictionary of your choice and make a copy of it.
fruits = {1:"apples", 2:"bananas", 3:"guavas", 4:"oranges", 5:"grapes", 6:"lemon", 7:"jackfruit"}
fruits_copy = fruits.copy()
print(fruits_copy)

#11.Write a python program to show nested dictionaries
student = {
    "name": "Agnes",
    "age" : 26,
    "course_units": {
        1: "Data Science",
        2: "Automation",
        3: "Data Analysis",
        4: "Artificial Intelligence"
	}
}