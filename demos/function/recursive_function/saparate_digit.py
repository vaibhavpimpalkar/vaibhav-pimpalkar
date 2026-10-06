def separate(n):
  if n==0:
    return 0
  # return separate(n%10)
  separate(n//10)
  print(n%10)
res=separate(121456445)
print(res)