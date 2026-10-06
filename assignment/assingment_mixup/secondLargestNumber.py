# List mein second largest number find karo.
# numbers=[12, 45, 7, 89, 23, 56]
# largest=numbers[0]
# second=numbers[0]

def secondLargest():
  numbers=[12, 45, 7, 89, 23, 56]
  largest=numbers[0]
  second=numbers[0]
  for i in numbers:
    if i>largest:
      second=largest
      largest=i
    elif i>second:
      second=i
  print(second)
secondLargest()













# for i in numbers:
#   if i>largest:
#     second=largest
#     largest=i
#   elif i>second:
#     second=i
# print(second)

    