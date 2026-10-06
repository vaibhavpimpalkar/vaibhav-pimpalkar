# Search for a number in a list. Use break when found and for-else to print "Not Found".

def found():
  numbers = [10, 20, 30, 40, 50]
  for i in numbers:
    if i==30:
      print("found!")
      break
  else:
   print("not found")
found()