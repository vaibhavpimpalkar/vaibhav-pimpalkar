# From a list, create two separate lists containing even and odd numbers.

def twoList():
 numbers= [12, 7, 20, 15, 30, 9, 44]
 even=[]
 odd=[]
 for i in numbers:
  if i%2==0:
   even.append(i)
  else:
   odd.append(i)
 print(even)
 print(odd)
twoList()