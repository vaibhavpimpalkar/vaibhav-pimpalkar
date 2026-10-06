# Write a recursive function to calculate the sum from 1 to n.

def recursive(n):
  if n==0:
    return 0
  return n+recursive(n-1)
result=recursive(5)
print(result)