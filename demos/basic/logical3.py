# WAP that takes a person age and checks their catagory 
# 1. if age 18 above and below 60 then print workin age
# 2.if age is below 18 or above 60 then not working age 
# 3.if age is exactly 60 then senior citizen

age = int(input("Enter Your age : "))

if age>=18 and age<60 :
  print("working age...")
elif age <18 or age>60 :
  print("Not working age...")
elif age==60:
  print("senior citizen")