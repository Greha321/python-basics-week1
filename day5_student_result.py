def calculate_result(marks):
    if marks >=40 :
        return "Pass"
    else :
        return "Fail"
students = [
    {"Name" : "Geeta","marks" : 42},
    {"Name" : "Srini","marks" : 20},
    {"Name" : "Riya", "marks" : 89}
]
for s in students:
    result = calculate_result(s["marks"])
    print(s["Name"],"=>",result)