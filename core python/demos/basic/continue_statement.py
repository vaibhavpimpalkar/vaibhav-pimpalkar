# for i in range(1,11):
#   if i==5:
#     continue
#   print(i)



#   for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(1, 3):
#         print("*", end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(i):
#         print(j, end=" ")
#     print()

# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)