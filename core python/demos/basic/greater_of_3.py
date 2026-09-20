# find greater no of three 

# x = 100
# y = 20
# z =30

x =int(input("Enter the value of x : "))
y=int(input("Enter the value of y :"))
z=int(input("Enter the value of z :"))


if x>y and x>z :
 print("x is greater : ")
elif y>x and y>z :
 print("y is greater : ")
elif z>x and z>y :
 print("z is greater : ")
else :
 print("Please enter diff value")