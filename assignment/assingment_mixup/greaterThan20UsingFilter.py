# filter() use karke list mein se 20 se greater numbers nikalo.

numbers = [10, 25, 5, 40, 15, 30]

result = filter(lambda x : x>20,numbers)
print(list(result))