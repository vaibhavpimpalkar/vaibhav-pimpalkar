# Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1=int(input("Enter you first subject marks : "))
sub2=int(input("Enter you second subject marks : "))
sub3=int(input("Enter you third subject marks : "))
sub4=int(input("Enter you fourth subject marks : "))
sub5=int(input("Enter you fifth subject marks : "))

sum = sub1+sub2+sub3+sub4+sub5 
percent = (sum/500)*100
print("percentage : "+str(percent))