import csv

try:
    with open("student_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        total_students = 0
        failed_count = 0
        count_A = count_B = count_C = count_D = count_F = 0

        for row in reader:
            name = row[0]
            marks = int(row[1])
            total_students += 1

            if marks >= 90:
                count_A += 1
                grade = "A"
            elif marks >= 75:
                count_B += 1
                grade = "B"
            elif marks >= 60:
                count_C += 1
                grade = "C"
            elif marks >= 40:
                count_D += 1
                grade = "D"
            else:
                count_F += 1
                failed_count += 1
                grade = "F"

            print(f"{name} got {marks} marks and grade {grade}")

        print("\nTotal Students:", total_students)
        print("Failed Students:", failed_count)
        print("Grades Count: A =", count_A, ", B =", count_B,
              ", C =", count_C, ", D =", count_D, ", F =", count_F)

except FileNotFoundError:
    print("File not found: student_data.csv")
