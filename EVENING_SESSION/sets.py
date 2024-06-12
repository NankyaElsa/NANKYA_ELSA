# Use the set() constructor to create a set of 3 of your favorite beverages
beverages = set(["Coffee", "Tea", "Soda"])

# Use the correct method to add 2 more items to the beverages set
beverages.add("Water")
beverages.add("Milk")

"""
Given the set below;
mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}
Check if microwave is present in the set.
"""
mySet = {"oven", "kettle", "microwave", "refrigerator"}
exists = "microwave" in mySet
print(exists)

# Write a python program to remove “kettle” from the set above
mySet.remove("kettle")

# Write a python program to loop through the set above
for item in mySet:
    print(item)

# Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set
set1 = {"apple", "banana", "cherry", "date"}
list1 = ["Tomato", "Orange"]

set1.update(list1)
print(set1)

# Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 35, 40, 50}
first_names = {"Rwakasiisi", "Sserunjogi", "Nankya", "Lutalo", "Otim"}

combined_set = ages.union(first_names)
print(combined_set)
