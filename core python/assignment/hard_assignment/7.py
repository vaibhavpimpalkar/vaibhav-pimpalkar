# Write a function using *args that returns the largest number.

def large(*args):
  largest=args[0]
  for i in args:
    if i>largest:
      largest=i
  return largest
    

print(large(10, 45, 23, 89, 56))