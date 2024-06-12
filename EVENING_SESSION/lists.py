"""
Exercise1 (Lists)

"""
#1.Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["Alec", "Athena", "Arita", "Arinda", "Anita"]
print(names[1])

#2.Write a python program to change the value of the first item to a new value
names[0] = "Amanda"
print(names)

#3.Write a python program to add a sixth item to the list
names.append("Athia")
print(names)

#4.Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")
print(names)

#5.Write a python program to remove the 4th item from the list
del names[3]
print(names)

#6.Use negative indexing to print the last item in your list
print(names[-1])

#7.Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
fruits = ["apples", "bananas", "guavas", "oranges", "grapes", "lemon", "jackfruit"]
print(fruits[2:5])

#8.	Write a list of countries and make a copy of it.
countries = ["Australia", "Canada", "Brazil", "Korea", "China"]
copy_countries = countries.copy()
print(copy_countries)

#9.Write a python program to loop through the list of countries
for country in countries:
    print(country)

#10.Write a list of animal names and sort them in both descending and ascending order.
animal_names = ["Lion","Elephant","Giraffe","Zebra","Cheetah","Hippopotamus","Crocodile","Buffalo","Rhino","Leopard"]
print("In ascending order")
sorted_animals = sorted(animal_names)
for animal in sorted_animals:
    print(animal)

print("In descending order")
for animal in sorted(animal_names, reverse=True):
    print(animal)

#11.Using the list above, write a python program to output only animal names with the letter ‘a’ in them
print("Animals with letter 'a'")
for animal in animal_names:
    if 'a' in animal:
        print(animal)

#12.Write two lists, one containing your first names and the other your second names. Join the two lists.
mysurname = ["Sserunjogi", "Nankya", "Otim", "Rwakasiisi", "Lutalo"]
mylastname = ["Hillal", "Elsa", "Ronald", "Edwin", "Allan"]
names = mysurname + mylastname
print(names)





