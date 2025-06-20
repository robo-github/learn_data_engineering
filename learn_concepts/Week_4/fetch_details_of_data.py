import csv

try:
    with open("student_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        total_students = 0
        count_A = 0
        count_B = 0
        count_C = 0
        count_D = 0
        count_F = 0
        passed_student = []
        failed_count = 0
        failed_student = []

        for row in reader:
            name = row[0]
            marks = int(row[1])
            total_students += 1

            if marks >= 90:
                grade = "A"
                count_A += 1
                passed_student.append((name, marks, grade))
            elif marks >= 75:
                grade = "B"
                count_B += 1
                passed_student.append((name, marks, grade))
            elif marks >= 60:
                grade = "C"
                count_C += 1
                passed_student.append((name, marks, grade))
            elif marks >= 40:
                grade = "D"
                count_D += 1
                passed_student.append((name, marks, grade))
            else:
                grade = "F"
                failed_count += 1
                count_F += 1
                failed_student.append((name, marks))

    print(f"📊 Total number of students : {total_students}")
    print(f"❌ Total number of students failed : {failed_count}")
    print()
    print(f"""
Total number of grades:
A Grade : {count_A}
B Grade : {count_B}
C Grade : {count_C}
D Grade : {count_D}
F Grade : {count_F}
""")
    for name, marks, grade in passed_student:
        print(f"🥳 {name} passed {marks} with {grade} grade.")
    print()
    for name, marks in failed_student:
        print(f"🥲  {name} failed with {marks}.")
    print()


except FileNotFoundError:
    print("FileNotFoundError: There is no file like student_data.csv")
