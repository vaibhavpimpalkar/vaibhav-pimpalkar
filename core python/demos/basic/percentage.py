# WAP to take marks of 5 subject from user and calculates 
# 1.total marks 
# 2.percentage
sub_one = int(input("Enter subject one : "))
sub_two = int(input("Enter sunject two : "))
sub_three = int(input("Enter sunject three : "))
sub_four = int(input("Enter sunject four : "))
sub_five = int(input("Enter sunject five : "))

total_marks = sub_one+sub_two+sub_three+sub_four+sub_five
print("Total marks : ",total_marks)

percentage = (total_marks/500)*100
print("Percentage : ",percentage)
