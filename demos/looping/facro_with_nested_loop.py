num=int(input("enter number : "))
sum=0

temp=num
while num>0:
  d=num%10
  num=num//10
  facto=1
  for i in range(1,d+1):
    facto*=i
  sum+=facto
if sum==temp:
  print(f"{temp} is strong number")
else:
  print(f"{temp} is not strong")
