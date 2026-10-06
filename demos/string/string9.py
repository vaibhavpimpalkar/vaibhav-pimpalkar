# count each vowel seperatly

text=input("enter text : ")
count = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

for i in text:
  if i in count:
    count[i]+=1
print(count)

# vowel="aeiou"

# count={}
# total=1
# for i in text:
#   if i in vowel:
#     if i=="a":
#       total+=1
#       count["a"]=total
#     elif i=="e":
#       total+=1
#       count["e"]=total
#     elif i=="i":
#       total+=1
#       count["i"]=total
#     elif i=="o":
#       total+=1
#       count["o"]=total
#     elif i=="u":
#       total+=1
#       count["u"]=total
# print(count)