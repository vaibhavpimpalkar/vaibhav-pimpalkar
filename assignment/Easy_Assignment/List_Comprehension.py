# Create a list containing squares of numbers 1–10 using list comprehension.

def square():
  no=[1,2,3,4,5,6,7,8,9,10]
  squ=[i**2 for i in no]
  print(squ)
square()
