# Given a nested dictionary:
# Print students whose age is greater than 25.

students = {
    "student1": {"name": "Amit", "age": 22},
    "student2": {"name": "Rahul", "age": 27},
    "student3": {"name": "Sneha", "age": 24}
}

for i in students:
  if students[i]["age"]>25:
    print(i,students[i])