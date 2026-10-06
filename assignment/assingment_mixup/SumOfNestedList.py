# Nested list ke saare numbers ka sum find karo.
numbers = [[10, 20], [5, 15, 25], [30, 40]]

def nested():
  add = 0 
  for i in numbers:
    for i in i:
      add+=i
  print(add)
nested()


# sum = 0
# for i in numbers:
#   for i in i:
    
#     sum+=i
# print(sum)