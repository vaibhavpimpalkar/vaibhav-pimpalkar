# Create a generator function called numbers() that produces:

# 1
# 2
# 3
# 4
# 5

def numbers():
   yield 1
   yield 2
   yield 3
   yield 4
   yield 5
for i in numbers():
   print(i)