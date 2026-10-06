# Create a dictionary containing name, age, and skill.
# Add a new key to an existing dictionary.
# Print all keys and values of a dictionary using a loop.

def dic():
  student={
    'name':'mr.bad',
    'age':18,
    'skill':'node js express mongodb python.'
  }
  student["pincode"]=445102
  for i in student:
    print(i,":",student[i])
dic()

