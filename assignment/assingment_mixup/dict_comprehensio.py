# Q1. Create a dictionary containing numbers from 1 to 5 as keys and their cubes as values.

numbers=range(1,6)
result={i: i*i*i for i in numbers}
print(result)

