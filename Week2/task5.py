students = []

for _ in range(3):
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")
    students.append((name, age, grade))

students_dict = {student[0]: (student[1], student[2]) for student in students}

print("Student details:")
for name, details in students_dict.items():
    print(f"Name: {name}, Age: {details[0]}, Grade: {details[1]}")
