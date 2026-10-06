# Create a dictionary from 1 to 10 where:

# even number → "Even"
# odd number → "Odd"

def demo():
  num = range(1,11)
  result={i: "even" if i%2==0 else "odd" for i in num}
  return result
print(demo())