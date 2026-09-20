# Create a dictionary containing only even numbers from 1 to 10, where:

# key = number
# value = square of number

# Expected output:

# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

def even():
  num = range(1,11)
  square = {i:i**2 for i in num if i%2==0}
  return square
print(even())