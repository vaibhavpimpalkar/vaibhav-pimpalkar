# lambda + map() use karke list ke saare numbers ke squares nikalo.
numbers = [2, 4, 6, 8]
square = map(lambda x:x**2,numbers)
print(list(square))