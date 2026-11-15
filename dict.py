student={
    "Name":"rahul",
    "Age":21,
    "Branch":"ECE"
}
print(student["Name"])

student["Age"]=24

print(student)
student.keys()
student.values()
student.items()
student.get("Name")
student.pop("Age")

for key, value in student.items():
    print(key, value)