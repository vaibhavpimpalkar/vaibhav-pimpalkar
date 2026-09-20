# Find the second largest unique number in a list without using sort() or max().

def unique():
  numbers = [12, 45, 7, 89, 23, 56, 89]
  largest=numbers[0]
  second=numbers[0]
  for i in numbers:
    if i > largest:
      second=largest
      largest=i
    elif i==largest:
      pass
    elif i>second:
      second=i
   
  print(second)
unique()