# find the number of word in a sentance 

text = input("enter string :")
count=0
for i in text:
  if i != " ":
    count+=1
  # else:
  #   count+=1
print(count)