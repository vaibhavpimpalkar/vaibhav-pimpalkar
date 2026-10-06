# 7. Find the sum of three-digit number.

digit = int(input("Enter three digit : "))

digit1 = digit % 10
print(digit1)


digit = digit//10
digit2=digit%10
print(digit2)

digit = digit // 10 
digit3=digit%10
print(digit3)

print("Sum of three digit : ", digit1 + digit2 + digit3)

