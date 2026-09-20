num=int(input("Enter number for seperation : "))
while(num>0):
  d=num%10
  print(f'digit : {d}')
  num = num//10
  print(f'num : {num}')