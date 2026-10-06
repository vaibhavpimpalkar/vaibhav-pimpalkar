# Find the largest number in a list without using max().

def larg():
  numbers = [12, 45, 7, 89, 23, 56]
  large=numbers[0]
  for i in numbers:
    if i>large:
      large=i
  print(large)
larg()