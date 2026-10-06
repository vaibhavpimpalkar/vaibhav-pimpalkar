# A calculator performs operations on numbers.

# Operations:

# 1 Add 2 Subtract 3 Multiply 4 Divide

# User enters numbers and chooses the operation.

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

print("Press number to perform calculation ")

print("Addition    : 1")
print("Subtraction : 2")
print("Multiply    : 3")
print("Division    : 4")
print("Remainder   : 5")

select=int(input("Enter perrformer : "))

if select ==1 :
  print(f"Additon of {num1} and {num2} is {num1+num2}.")
elif select==2:
  print(f"Subtraction of {num1} and {num2} is {num1-num2}.")
elif select==3:
  print(f"multiplication of {num1} and {num2} is {num1*num2}.")
elif select==4:
  print(f"Division of {num1} and {num2} is {num1/num2}.")
elif select==5:
  print("remainder is : ", num1%num2)