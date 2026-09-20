# Create a generator that produces numbers from 1 to 5 using a for loop inside the generator.

def num():
  for i in range(1,6):
    yield i
for i in num():
  print(i)