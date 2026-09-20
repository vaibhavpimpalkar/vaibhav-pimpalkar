# Given a nested list:

# numbers = [[10, 20], [30, 40], [50, 60]]

# Find the total sum of all elements using nested loops.

def add():
  numbers = [[10, 20], [30, 40], [50, 60]]
  total=0
  for row in numbers:
    for value in row:
      total+=value
  print(total)
add()