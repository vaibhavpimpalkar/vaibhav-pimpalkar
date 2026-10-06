# 🔥 Hard Question #4 — ATM Withdrawal System

# User se input lo:

# Enter balance:
# Enter withdrawal amount:
# Enter PIN:
# Rules:

# 1. PIN check

# Correct PIN = 1234
# Wrong PIN → Incorrect PIN

# 2. Agar PIN correct hai:

# Withdrawal amount <= 0 → Invalid Amount
# Withdrawal amount balance se zyada → Insufficient Balance
# Withdrawal amount ₹100 ke multiple mein nahi hai → Amount must be multiple of 100
# Otherwise withdrawal successful.

# 3. Withdrawal ke baad:

# New balance >= 5000 → Healthy Balance
# New balance >= 1000 → Normal Balance
# New balance < 1000 → Low Balance


balance = int(input("Enter balance : "))
amount=int(input("Enter withdrawal amount : "))
pin =int(input("Enter pin : "))

if pin ==1234:
  if amount<=0:
    print("Invalid Amount ")
  elif balance<amount:
    print("Insufficient Balance")
  elif amount%100!=0:
    print("Amount must be multiple of 100")
  else:
    print("Withdrawal successful")
    balance=balance-amount
    print("Remaining Balance : ",balance)
    if balance>=5000:
      print("Healthy Balance")
    elif balance>=1000:
      print("Normal balance")
    else:
      print("Low Balance")
else:
  print("Incorrect Pin")
