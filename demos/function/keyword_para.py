# 1. To neglect positional parameter concept
# 2.Assign value to para in function callable

def emp(id,name,sal,dept):
  return f'ID:{id}\nNAME:{name}\nSALARY:{sal}\nDEPARTMENT:{dept}'
res=emp(name='VAIBHAV',sal=35000,id=101,dept="IT")
print(res)