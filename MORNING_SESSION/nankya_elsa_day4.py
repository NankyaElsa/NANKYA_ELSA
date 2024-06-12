#This script talks about dictionaries in python

#Dictionaries
#Creating and using dictionaries
#Dictionary methods and operations

"""
Dictionaries in python are collections of keys and values
-unordered
-mutable and 
indexed by keys

"""
#Example 1
#Create a dictionary for a student persuing software  engineering,
# the key must be your name, age, technology interest, course and year of study.
# put your own details

student_details = {
    "name": "Elsa",
    "age": "22",
    "technology": "Data SCience and ML",
    "course": "BSSE",
    "year":"year3"
    }
#access values in  a dictionary
print(student_details["name"])
print(student_details["age"])

#modify values
#Exercise 1: Modify age and technology
student_details["age"] = "36"
student_details["technology"] = "Web development"
print(student_details)

#Example2: Adding keys and values
student_details["email"] = "nankyaelsa1@gmail.com"
print(student_details)

#Exercise2 Remove a key and value from dictionary
#using remove/del
del student_details['age']
print(student_details)

#using pop
#student_details.pop("course")
#print(student_details)

#Common dictionary methods
"""
get() - returns the value for the specified key if the key is in the 
dictionary, if not it returns none or a default value if any is 
specified

update() - updates the dictionary with the elements from another
dictionary

pop() - removes the specified key and returns the corresponding value

"""
#Example 3: Use the get method to get the value
name =  student_details.get("name")
print(name)

# Exercise 3: Use the update method to change value of age
student_details.update({"age":"19"})
print(student_details["age"])

# Exercise 4: Use the if to check if the key 'age' 
# is present in the dictionary
if "age" in student_details:
    print("Key age is in student details dictionary")
else:
    print("Key age is not in the student details dictionary")

#keys(), values() and items() methods
"""
keys() - returns a view of objects that displays a list of all keys in the dictionary

values() - returns a view of objects that displays a list of all values in the dictionry

items() - returns a view of objects that displays a list of dictionary keys and
values tuple pairs

"""
#how these methods are used
all_keys = student_details.keys()
print(all_keys)
all_values = student_details.values()
print(all_values)
all_pairs = student_details.items()
print(all_pairs)

#Exercise 5
#Use the update method to change the course and add a new 
#key "WhatsApp_Number" to the dictionary

student_details.update({"course":"CSC", "whatsapp_number":"0774344558"})
print(student_details)






