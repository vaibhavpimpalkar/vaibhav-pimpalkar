# 11. Write a program to accept an integer amount from user and tell minimum
#     number of notes needed for representing that amount..


notes = int(input("Enter Rupees : "))
cash500 = notes//500

print("notes of 500 : ",cash500)
notes = notes%500
cash100=notes//100
print("Notes of 100 : ",cash100)

notes=notes%100
cash50=notes//50
print("Notes of 50 : ",cash50)

notes=notes%50
cash20=notes//20

print("Notes of 20 : ",cash20)

notes=notes%20
cash10=notes//10
print("Notes of 10 : ",cash10)