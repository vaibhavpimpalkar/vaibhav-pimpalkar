# Write a Program to input two angles from user and find third angle of the triangle

angle_1 =int(input("Enter first angle : "))
angle_2 =int(input("Enter second angle : "))

angle_3=180-(angle_1+angle_2)
print("Third angle of trangle is : ",angle_3)