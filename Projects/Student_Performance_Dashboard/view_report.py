import csv
import os

# Get the folder this script is in
base_path = os.path.dirname(os.path.abspath(__file__))
# Full path to the CSV file inside the 'data' folder
csv_path = os.path.join(base_path, "data", "student_report.csv")

try:
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        next(reader)

        total_student = 0
        count_a = count_b = count_c = count_d = count_f = 0
        passed_count = 0
        failed_count = 0
        passed_student = []
        failed_student = []

        for row in reader:
            name = row[0]
            marks = int(row[1])
            grade = row[2]
            remark = row[3]
            total_student += 1

            if grade == "A":
                count_a += 1
                passed_count += 1
            elif grade == "B":
                count_b += 1
                passed_count += 1
            elif grade == "C":
                count_c += 1
                passed_count += 1
            elif grade == "D":
                count_d += 1
                passed_count += 1
            if grade != "F":
                passed_student.append((name, marks, grade, remark))
            else:
                count_f += 1
                failed_count += 1
                failed_student.append((name, marks, grade, remark))

    print(f"Total Numbers of students : {total_student}")
    print(f"""
Number of students in each grade :
 A Grade = ({count_a}) , B Grade = ({count_b}) , C Grade = ({count_c}) , D Grade = ({count_d}) , F Grade = ({count_f})
""")
    print(f"📊 Passed : {passed_count} | ❌ Failed : {failed_count}")
    print()
    print("Passed Students Details :")
    for name, marks, grade, remark in passed_student:
        print(f"✅ {name} passed with {marks}. Grade : {grade} {remark} ")
    print()
    print("Failed Student Details :")
    for name, marks, grade, remark in failed_student:
        print(f"❌ {name} failed with {marks}. Grade : {grade} {remark}")

except FileNotFoundError:
    print("FileNotFoundError: student_report.csv not found.")
