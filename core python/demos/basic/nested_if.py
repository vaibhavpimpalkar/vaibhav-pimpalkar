# Wap for login take username and password from user 
# 1. if username is "admin" then check the password
# 2.if password is "1234" then print "login successful"
# 3.otherwise print wrong password
# 4. if username is not admin then print invalid username 

username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" :
  if password== "1234":
    print("login successful....")
  else:
    print("Wrong password...")
else :
  print("invalid username....")
