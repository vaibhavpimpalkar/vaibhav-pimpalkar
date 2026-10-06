# num=int(input("Enter number : "))
# facto=1
# for i in range(1,num+1):
#   facto*=i
# print(facto)


# num = int(input("Enter  number: "))
# while num>0:
#   d=num%10
#   print("digit : ",d)
#   num //=10

# num=int(input("Enter number : "))
# a=-1
# b=1
# for i in range(num):
#   c=a+b
#   print(c,end=" ")
#   a=b
#   b=c

# num=int(input("Enter number :"))
# if num>1:
#   for i in range(2,num//2+1):
#     if num%i==0:
#       print(" not prime")
#       break
#   else:
#     print("prime")
# else:
#   print("prime")

# num=int(input("enter number : "))
# sum=0
# temp=num
# while num>0:
#   d=num%10
#   num=num//10
#   facto=1
#   for i in range(1,d+1):
#     facto*=i
#   sum+=facto
# if sum==temp:
#   print("prime")
# else: 
#   print("not prime")




# 7.WAP to print all integers upto n that aren’t divisible by 2 and 3. 

# n= int(input("enter number : "))
# for i in range(1,n+1):
#   if (i%2!=0 and i%3!=0):
#     print(i,end=" ")
  # else:
  #   print("no")

# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range

number=int(input("enter number : "))
for i in range(1,number+1):
  if i%7==0 and i%5==0:
    print(i,end=" ")

