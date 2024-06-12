#Concatenating 2 variables
print("-----------Concatenating----------")
name = "Allan"
brothers = 2

print(name +" has " + str(brothers) +" brothers.")

#Removing space Characters
print("-----------Removing space characters----------")
txt = "   Hello,    Uganda!    "

#Using replace method
print("-----------Using replace method----------")
txt_no_Space = txt.replace(" ","")
print(txt_no_Space)

#Using split() and join() method 
print("-----------Using split() and join() method----------")
txt_noSpace = "".join(txt.split())
print(txt_noSpace)

#Change to UpperCase
print("-----------Change to UpperCase----------")
print(txt.upper())

#Replacing a value
print("-----------Replacing a value----------")
print(txt.replace("U", "V"))

#Returning a character by index
print("----------Returning a character by index-------------")
y = "I am proudly a Ugandan"
print(y[1:4])

#Correcting an error
x = "All “Data Scientists” are cool!"
print(x)

#corrected code using 
#Using escape characters
print("-----------Correcting code using escape characters----------")
corrected1 = "All \"Data Scientists\" are cool"
print(corrected1)

#Using single quotes
print("-----------Correcting code using single quotes----------")
corrected2 = 'All "Data Scientists" are cool'
print(corrected2)