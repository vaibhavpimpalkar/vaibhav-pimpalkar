# Use lambda + map() to convert:
# [2, 4, 6, 8]

# into their squares.

def square():
  numbers = [2, 4, 6, 8]
  result=map(lambda x:x**2,numbers)
  print(list(result)) 
square()