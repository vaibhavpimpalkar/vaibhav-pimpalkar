# WAP that takes age and has_id from user
# .if age is 18 or above and the person has an ID then "You can enter "
# otherwise "You cannot enter"

age = int(input("Enter your age : "))
has_id = input("You have ID : ")

if age>18 and has_id == "yes":
  print("You can enter ...........")
else :
  print("You cannot enter..")