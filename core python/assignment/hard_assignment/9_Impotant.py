# Write a recursive function to calculate factorial.

def factorial(n):
  if n==0:
    return 1
  fact=n*factorial(n-1)
  return fact
result=factorial(5)
print(result)