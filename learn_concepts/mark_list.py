import csv

try:
    with open("student.csv", "r") as file:
        reader = csv.reader(file)
        fail_count = 0
        pass_count = 0
        fail_student = []

        print("🎓 Student Grades: ")
        for row in reader:
            name = row[0]
            marks = int(row[1])
            if marks >= 80:
                grade = "A"
                remark = "Excellent"
                pass_count += 1
            elif marks >= 60:
                grade = "B"
                remark = "Good"
                pass_count += 1
            elif marks >= 40:
                grade = "D"
                remark = "Pass"
                pass_count += 1
            else:
                grade = "F"
                remark = "Fail"
                fail_count += 1
                fail_student.append((name, marks))
            print(f"Name: {name}, Marks: {marks} → Grade: {grade} ({remark})")
        print()

        for name, mark in fail_student:
            print(f"😢 {name} failed with {mark} marks.")
        print()
    print()
    print(f"📊 Passed: {pass_count} | Failed: {fail_count}")

except FileNotFoundError:
    print("File not found")
