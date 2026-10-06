def sumOfseries(n):
  if n==0:
    return 0
  return n + sumOfseries(n-1)
res=sumOfseries(5)
print(res)