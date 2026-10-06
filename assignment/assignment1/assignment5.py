# Write a program to enter P, T, R and calculate Compound Interest.

p=int(input("Enter value of p :"))
t=int(input("Enter value of t :"))
r=int(input("Enter value of r :"))

compound_interest = (p*((1+r/100)**t))-p

print("Compund interest : ",compound_interest)
