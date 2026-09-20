# 🔥 Challenge: Student Result + Scholarship

# User se input lo:

# Marks
# Attendance (%)



# Rules:

# Step 1 — Marks check

# Marks < 0 or > 100 → Invalid Marks
# Otherwise continue.

# Step 2 — Result

# Marks < 40 → Fail
# Marks >= 40 → Pass

# Step 3 — Agar Pass hai, attendance check karo

# Attendance < 75 → Pass but Not Eligible
# Attendance >= 75 → Eligible

# Step 4 — Eligible students ke liye grade

# 90–100 → A
# 75–89 → B
# 60–74 → C
# 40–59 → D

# Step 5 — Scholarship

# Scholarship milegi agar:

# Marks >= 85 AND Attendance >= 90

# Otherwise:

# No Scholarship

marks = float(input("Enter marks : "))
attendance = float(input("Enter attendance in percen : "))

if marks<0 or marks>100:
  print("Invalid marks")
elif attendance<0 or attendance>100 :
  print("Invalid attendance")
elif marks<40 :
  print("Fail")
else:
  print("pass")
  if attendance<75:
    print("pass but not eligible")
  else :
    print("Eligible")
    if marks>=90:
      print("Grade A")
    elif marks>=75:
      print("Grade B")
    elif marks>=60:
      print("Grade C")
    else:
      print("Grade D")

    if marks>=85 and attendance>=90:
      print("Eligible for scholarship")
    else:
      print("no scholarship")
      

