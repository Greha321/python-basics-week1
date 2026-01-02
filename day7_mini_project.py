students = []

def add_student(name, marks):
    student = {"name": name, "marks": marks}
    students.append(student)

def show_students():
    for s in students:
        result = "Pass" if s["marks"] >= 40 else "Fail"
        print(s["name"], "-", s["marks"], "-", result)

add_student("Ram", 78)
add_student("Ali", 35)
add_student("Sara", 62)

show_students()
