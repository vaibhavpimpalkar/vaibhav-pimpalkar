### MAP with LAMBDA

# 1.to reduce the lines of code
# 2. perform same task multiple times on different input
# 3.return object we have convert into list 



def sq(n):
  return n*n

data=[1,2,3,4,5,6,7,8,9,10]

#  METHOD 1 :
res=list(map(sq,data))
print(res)

# METHOD 2 :

res=list(map(lambda n:n*n,data))
print(res)

