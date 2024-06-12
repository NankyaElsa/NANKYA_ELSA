x= ("samsung", "iphone", "tecno","redmi")
myFavorite = "iphone"
if myFavorite in x:
    print ("My favourite brand is : "+myFavorite)
else:
    print("Not in the list")


list_from_turple = list(x)
for i in range(len(list_from_turple)):
    if list_from_turple[i] == "iphone":
        list_from_turple[i] = "Infinix"
x = tuple(list_from_turple)
print(x)

x = list(x)
x.append("Huawei")
x = tuple(x)
print(x)

for i in range(len(x)):
    print(x[i])

index_to_remove = 0
x = list(x)
x.pop(index_to_remove)
x = tuple(x)
print(x)


cities_in_uganda = tuple(["Kampala","Jinja","Mbale","Mbarara","Gulu","Lira","Arua","Masaka","Entebbe","Fort Portal"])
for city in cities_in_uganda:
    print(city)


listed = list(cities_in_uganda)
print(listed[2:5])



myFirstName =( "Hillal",)
myLastName = ("Sserunjogi",)

myFullName = myFirstName + myLastName
print(myFullName)



colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)



thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print("The number of times * appears is : ",count)
