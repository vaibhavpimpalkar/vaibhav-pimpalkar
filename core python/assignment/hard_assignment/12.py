# Use lambda + filter() to find numbers divisible by both 2 and 3.

def divisible(*numbers):
  result=filter(lambda x:x%2==0 and x%3==0,numbers)
  print(list(result))
divisible( *[6, 10, 12, 15, 18, 20, 24])