# names = ["Vaibhav", "Amit", "Raj", "Sneha"]

# Create a dictionary where:

# key = name
# value = length of the name

def demo():
  names = ["Vaibhav", "Amit", "Raj", "Sneha"]
  result={i:len(i) for i in names}
  return result
print(demo())