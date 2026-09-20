# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("enter book price : "))
discount=int(input("Enter discount : "))

discount_price=(cost_price*discount/100)
selling_price = cost_price-discount_price

print("Selling price : ",selling_price)