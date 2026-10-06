# 7. Program to Find the Roots of a Quadratic Equation

a=float(input("Enter a : "))
b=float(input("Enter b : "))
c=float(input("Enter c : "))

d=b**2-4*a*c

root2 =(-b-d**0.5)/(2*a)
root1 =(-b+d**0.5)/(2*a)

print("Root_1 : ",root1)
print("Root_2 : ",root2)