# Number search karo: mil gaya to break, nahi mila to for-else se "Not Found" print karo.

def find(*number):
  for i in number:
    if i == 30:
      print("Found")
      break
  else:
    print("not found")
find(10, 20, 30,  40, 50)