# Ek function banao jo 2 numbers ka sum return kare.

a=int(input("enter a :"))
b=int(input("enter b :"))

def sum(*args):
  add = 0
  for i in args:
    add+=i
  print(add)
sum(a,b)
