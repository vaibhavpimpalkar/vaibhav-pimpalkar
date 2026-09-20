# 1. Convert the time entered in hh,min and sec into seconds.

hour=int(input("Enter hour : "))
minute=int(input("Enter minute : "))
second=int(input("Enter second : "))

hour=hour*3600
minute=minute*60
second=hour+minute+second
print("Total Second : ",second)


# time = int(input("Enter time : "))

# time = float(input("Enter time : "))

# hour = time//60
# remaining_time = time%60

# print("hour : ",hour)

# minute=remaining_time//60

# print("Minute : ",minute)

# second=remaining_time%3600

# print("Second : ",second)