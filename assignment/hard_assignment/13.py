# Write a function that returns minimum, maximum, and average of a list.
def lis():
  numbers = [10, 20, 30, 40, 50]
  length = len(numbers)
  length=int(length)
  total=0
  for i in numbers:
    total+=i
  avrage=total/length
  return min(numbers),max(numbers),avrage
print(lis() )