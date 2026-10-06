# 10. Write a program to reverse three-digit number.
a = 123

last=a%10
a=a//10
print("a : ",a)
print("last digit : ",last)

sec = a%10
a=a//10
print("a : ",a)
print("Second digit : ",sec)

first=a%10
a=a//10
print("a : ",a)
print("First digit : ",first)

reverseStr = str(last)+str(sec)+str(first)
reverseStr=int(reverseStr)
print(reverseStr)