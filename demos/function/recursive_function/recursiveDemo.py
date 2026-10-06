n=5

def fun(n):
  print("function execting")
  if n>1:
    fun(n-1)
fun(n)