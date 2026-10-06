# Use map() and filter() together to:
# first select even numbers
# then square those numbers.

def assignment():
  numbers = [1, 2, 3, 4, 5, 6]
  even = filter(lambda x:x%2==0,numbers)
  even = list(even)
  square = map(lambda x:x**2,even)
  print(even)  
  print(list(square))
assignment()