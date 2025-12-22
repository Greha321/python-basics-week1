students = []

student1 = {"Name":"RAM", "Marks" : 85}
student2 = {"Name":"RAJU", "Marks" : 75}

students.append(student1)
students.append(student2)

for s in students :
    print(s["Name"],"Scored", s["Marks"])
    