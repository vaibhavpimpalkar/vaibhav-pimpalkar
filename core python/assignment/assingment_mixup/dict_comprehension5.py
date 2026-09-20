# Create a dictionary containing only numbers divisible by 3, where:

# key = number
# value = "Divisible by 3"

def demo():
  num=range(1,11)
  result={i:"Divisible by 3" for i in num if i%3==0}
  return result
print(demo())