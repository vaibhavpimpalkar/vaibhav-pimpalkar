# 🔥 Hard Practice #2 — Triangle

# User se three angles input lo aur determine karo:

# Agar sum 180 nahi hai → Invalid Triangle
# Sum 180 और सभी angles equal → Equilateral
# Sum 180 और कोई दो angles equal → Isosceles
# Sum 180 और सभी अलग → Scalene


a=int(input("Enter angle 1 :" ))
b=int(input("Enter angle 2 : "))
c=int(input("Enter angle 3 : "))

if a+b+c != 180 :
  print("Invalid Triangle")
elif a==b and b==c :
  print("Equilateral")
elif a==b or b==c or a==c :
  print("Isosceles")
else :
  print("Scalene")