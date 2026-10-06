# ATM Machine
# An ATM machine allows users to:

# 1 Check balance 2 Withdraw money 3 Deposit money 4 Exit

# We will simulate a simple ATM program.

balance = 150000

print("1 Check balance")
print("2 Withdraw money")
print("3 Deposit money")
print("4 Exit")

choose=int(input("Enter option : "))

if choose==1:
  print("Your balance is : ",balance)
elif choose==2:
  if balance>0:
    amount=int(input("ENter amount :"))
    if amount<balance:
      balance=balance-amount
      print("withdaw successful ")
      print("your balence is : ", balance)
    else: 
      print("amount is grater than the balance")
elif choose==3:
  amount=int(input("Enter amount :"))
  balance=balance+amount
  print("deposit successful ")
  print("Your balance is : ",balance)
elif choose==4:
  print("Thank you for banking")