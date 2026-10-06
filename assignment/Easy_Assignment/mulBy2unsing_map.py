# Use map() to multiply every number in a list by 2.

def mul():
  no=[231,56,84,56]
  mult=map(lambda x:x*2,no)
  mult= list(mult)
  print(mult)
mul()