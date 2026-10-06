# count vowels in string
text=input("enter text : ")
vowel="aeiouAEIOU"
count=0
for i in text:
  if i in vowel:
    count+=1
print(count)