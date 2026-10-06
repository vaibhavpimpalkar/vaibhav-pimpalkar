# Print only even numbers from a list.

def even():
  numbers = [12, 7, 20, 15, 30, 9, 44]
  for i in numbers:
    if i %2==0:
      print(i)
even()