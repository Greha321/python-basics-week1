def add_student(name, marks):
    file = open("students.txt", "a")
    file.write(name + "," + str(marks) + "\n")
    file.close()

def show_students():
    file = open("students.txt", "r")
    for line in file:
        name, marks = line.strip().split(",")
        print(name, "=>", marks)
    file.close()

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        add_student(name, marks)

    elif choice == "2":
        show_students()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
