import csv
from datetime import datetime
import os

# Get path to the folder this script is in
base_path = os.path.dirname(os.path.abspath(__file__))
# Make the path to the data folder
data_folder = os.path.join(base_path, "data")
# Create the folder if it doesn't exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)


def log_message(message):
    time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    log_path = os.path.join(data_folder, "log_report.txt")
    with open(log_path, "a") as logfile:
        logfile = logfile.write(f"[{time}] {message}\n")


while True:
    name = input("Enter the name of student or (Type 'exit' to stop): ")
    if name.lower() == "exit":
        print("You are exit.")
        print()
        break

    try:
        marks = int(input("Enter the mark of the student : "))
        if 0 <= marks <= 100:
            if marks >= 90:
                grade = "A"
                remark = "Excellent"
            elif marks >= 75:
                grade = "B"
                remark = "Very good"
            elif marks >= 60:
                grade = "C"
                remark = "Good"
            elif marks >= 40:
                grade = "D"
                remark = "Pass"
            else:
                grade = "F"
                remark = "Fail"
            csv_path = os.path.join(data_folder, "student_report.csv")
            with open(csv_path, "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, marks, grade, remark])
            print("Record saved")
            print()
            log_message(
                f"{name} ({marks}) -> Grade : {grade} saved to student_report.csv")
        else:
            print("Mark must be in 0 to 100.")
            print()
            log_message(f"Invalid marks {marks} entered by student '{name}'.")

    except ValueError:
        print("Please Enter a valid integer for marks.")
        print()
        log_message("Invalid input: non-integer marks entered.")
