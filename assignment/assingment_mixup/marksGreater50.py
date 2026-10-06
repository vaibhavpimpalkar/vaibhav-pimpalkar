# Dictionary mein students ke names aur marks hain. 50 se zyada marks wale students print karo.

def marks():
    students = {
    "Rahul": 45,
    "Amit": 72,
    "Sneha": 65,
    "Raj": 38
}
    for i in students:
        if students[i]>50:
            print(i,students[i])
marks()