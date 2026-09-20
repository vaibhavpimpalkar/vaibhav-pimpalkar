# Write a Python program that takes units consumed as input and calculates the electricity bill according to these slabs:
# Unit        Rate
# 0–100       ₹5 per unit
# 101–200     ₹7 per unit
# Above 200   ₹10 per unit

unit =int(input("Enter electricity unit : "))

if unit<=100 :
  print("Bill : ",unit*5,"rupees")
elif unit>100 and unit<=200 :
  print("Bill : ",unit*7,"rupees")
elif unit>200:
  print("Bill : ",unit*10,"rupees")