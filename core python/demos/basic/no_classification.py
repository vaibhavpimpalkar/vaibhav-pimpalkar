# 🔥 Hard Practice #3 — Number Classification

# User se integer lo:

# Positive + Even → Positive Even
# Positive + Odd → Positive Odd
# Negative + Even → Negative Even
# Negative + Odd → Negative Odd
# 0 → Zero

num = int(input("Enter number : "))

if num>0 :
  if num%2==0:
    print("number is positive even  : ",num)
  else :
    print("Number is positive odd : ",num)
elif num<0:
  if num%2==0:
    print("Number is negative even  : ",num)
  else:
    print("Number is negative  odd: ",num)
else:
  print("zero")

    

