# 🔥 Hard Question #5 — Electricity + Customer Type

# User se:

# Units consumed
# Customer type

# input lo.

# Customer type:

# 1 → Residential
# 2 → Commercial

# Residential rates:

# 0–100 → ₹5/unit
# 101–200 → ₹7/unit
# Above 200 → ₹10/unit

# Commercial rates:

# 0–100 → ₹8/unit
# 101–200 → ₹12/unit
# Above 200 → ₹15/unit

# Phir:

# Units < 0 → Invalid
# Bill > ₹2000 → 10% surcharge
# Bill > ₹5000 → 15% surcharge
# Otherwise → No surcharge

# unit_consumed=int(input("Enter unit : "))
# if unit_consumed <0:
#   print("Invalid")
# else : 
#   print("1.Residential :")
#   print("2.Commercial  :")

#   customer_type = int(input("Enter type :"))
#   if customer_type==1:
#     if unit_consumed<=100:
#       bill=unit_consumed*5
#     elif unit_consumed <=200:
#       bill=unit_consumed*7
#     else :
#       bill=unit_consumed*10
#   elif customer_type==2:
#     if unit_consumed<=100:
#       bill=unit_consumed*8
#     elif unit_consumed <=200:
#       bill=unit_consumed*12
#     else:
#       bill=unit_consumed*15

#   if bill>5000:
#     surcharge = bill*15/100
#     total_bill=surcharge+bill
#   elif bill > 2000:
#     surcharge = bill*10/100
#     total_bill= bill+surcharge

   

#     print(f"your bill : {total_bill}")
#   else:
#     print("please press 1 or 2")
# total_bill = bill
# print(f"your bill : {total_bill}")
  # if bill>5000:
  #   surcharge = bill*10/100
  #   total_bill=surcharge+bill
  # elif bill > 2000:
  #   surcharge = bill*15/100
  #   total_bill= bill+surcharge

  # total_bill=bill

  # print(f"your bill : {total_bill}")

  

unit_consumed = int(input("Enter unit: "))

if unit_consumed < 0:
    print("Invalid")

else:
    print("1. Residential")
    print("2. Commercial")

    customer_type = int(input("Enter type: "))

    if customer_type == 1:

        if unit_consumed <= 100:
            bill = unit_consumed * 5

        elif unit_consumed <= 200:
            bill = unit_consumed * 7

        else:
            bill = unit_consumed * 10

    elif customer_type == 2:

        if unit_consumed <= 100:
            bill = unit_consumed * 8

        elif unit_consumed <= 200:
            bill = unit_consumed * 12

        else:
            bill = unit_consumed * 15

    else:
        print("Please press 1 or 2")
        bill = 0

    # Surcharge
    if bill > 5000:
        surcharge = bill * 15 / 100
        total_bill = bill + surcharge

    elif bill > 2000:
        surcharge = bill * 10 / 100
        total_bill = bill + surcharge

    else:
        total_bill = bill

    print(f"Your bill: ₹{total_bill}")