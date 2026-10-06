# names = ["Rahul", "Amit", "Vaibhav", "Rohit"]

# for i in names:
#   print(i)


# numbers = [10, 20, 30, 40, 50]
# for i in numbers:
#   print(i)  

# numbers = [10, 20, 30, 40, 50]
# for i in numbers:
#   if i>25:
#     print(i)

# numbers = [11, 20, 33, 42, 55, 60, 71, 80]
# for i in numbers:
#   if i%2!=0:
#     print(i)

# numbers = [1, 2, 3, 4, 5]
# even =[i%2==0 for i in numbers]
# print(even)

# numbers = [10, 15, 20, 25, 30, 35]
# big=[i for i in numbers if i>20]
# print(big)

# no = [1,2,3,4,5,6,7,8,9,10]
# square=[i*i for i in no]
# print(square)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd=[i for i in numbers if i%2!=0]
# print(odd)

a = [10, 20, 30]
b = a
print(a)
b.append(40)

print(a)
print(b)