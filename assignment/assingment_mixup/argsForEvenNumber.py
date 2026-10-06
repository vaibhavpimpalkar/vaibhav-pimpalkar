# \*args use karke function banao jo diye gaye numbers mein se even numbers return kare.

def even(*args):
  for i in args:
    if i%2==0:
      print(i)

even(656,56565,6556156,56651,)