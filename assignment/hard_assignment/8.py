# Write a function using **kwargs that prints all student information.

def stud(**kwargs):
  for i in kwargs:
    print(i,"=",kwargs[i])
result=stud(name="Amit", age=22, skill="Python")
print(result)
