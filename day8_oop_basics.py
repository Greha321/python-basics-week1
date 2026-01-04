class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def show_result(self):
        if self.marks >= 40:
           return "Pass"
        else:
            return "Fail"
s1 = Student("Ram", 90)
s2 = Student("Anand", 56)

print(s1.name, s1.show_result())
print(s2.name, s2.show_result())