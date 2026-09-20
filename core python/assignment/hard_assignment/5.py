# Given two sets, find:
# Union
# Intersection
# Difference
# Symmetric difference

def twoSets():
  a = {1, 2, 3, 4}
  b = {3, 4, 5, 6}
  Union=a.union(b)
  Inter=a.intersection(b)
  diff=a.difference(b)
  symm=a.symmetric_difference(b)

  print(Union)
  print(Inter)
  print(diff)
  print(symm)
twoSets()


