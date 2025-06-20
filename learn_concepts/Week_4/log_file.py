from datetime import datetime
import csv


def log_message(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as logfile:
        logfile.write(f"[{time}] {message}\n")


try:
    name = input("Enter the student name: ")
    marks = int(input("Enter marks:"))

    if 0 <= marks <= 100:
        with open("student.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, marks])
        print("Student record saved.")
        log_message(
            f"Student '{name}' with marks {marks} saved to students.csv")
    else:
        print("❌ Mark must be between 0 and 100.")
        log_message(f"Invalid marks ({marks}) entered for student '{name}'")
except ValueError:
    print("❌ Please enter a valid integer for marks.")
    log_message("Invalid input: non-integer marks entered.")
