# string : - sequence of charater enclosed inside quotes.

name="vaibhav"
for i in name:
  print(i)
print("__________________indexing______________________________")
print(name[0])
print(name[-1])

print("___________________slicing_____________________________")

# slicing : used to extract a part of a string.

print(name[0:5])
print(name[4::-1])# vaibhav
print(name[:2])
print(name[::-1])
print(name[::-2])

print("_________________upper and lower_______________________________")

print(name.upper())
print(name.lower())


print("_________________strip_______________________________")

# strip is used to removes spaces from begining and ending.
name="shanta bai    "
print(name)
print(name.strip())

print("_____________________replace___________________________")
# replace is used to replace one value with another

print(name.replace("shanta","shanti"))
print(name.replace("shanta ","python "))



print("____________________split____________________________")
# split is used to convert string into list 

print(name.split()) #output  :   ['shanta', 'bai']

print("__________________join____________________")
text=['i','am','developer']
print(" ".join(text))

text1="im vaibhav"
print(" ".join(text1))

print("____________find_________________")

print(name.find("b"))

print("___________count__________________")
print(name.count("i"))
print(name.count("a"))

print(name.startswith("sh")) # output gives in bool


# print(name[0]="h")# gives error because of string is immutable 
print(name[0]=="s")#gives output in bool

print("_______________string membership_______________")
# string membership checks whether a character or substring exist 
print("s" in name)
print("x" not in name)
print("x" in name)