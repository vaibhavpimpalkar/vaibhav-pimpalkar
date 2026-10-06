# Create a set containing the squares of numbers from 1 to 10.
def demo():
  num=range(1,11)
  result={i*i for i in num}
  return result
  # print(result)
print(demo())