import pandas as pd
import os
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'students6.csv')

df = pd.read_csv(csv_path)

# Log function


def log_message(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join(base_dir, 'data', 'student_log.txt')
    with open(log_path, "a", encoding="utf-8") as logfile:
        logfile.write(f"[{time}] {message}\n")


def show_all_students():
    print("\n📃 All Students:")
    print(df["Name"])


def show_sorted_students():
    sorted_students = df.sort_values(by="Name", ascending=True)
    print("\n 📌 Sorted Students:")
    print(sorted_students)


def show_subjectwise_average():
    show_subjectwise = df.groupby("Subject")["Marks"].mean().round()
    print("\n🟰 Subject-wise Average Marks:")
    print(show_subjectwise)


def show_failed_students():
    failed_students = df[df["Marks"] < 20]
    print("\n❌ Failed Students:")
    print(failed_students)


def show_top_score():
    top_score = df.sort_values(by="Marks", ascending=False).head(3)
    print("\n🏆 Toppers:")
    print(top_score)


try:
    while True:
        print("\n📋 Student Data Analyzer Menu")
        print("1. Show all students")
        print("2. Show sorted student Names")
        print("3. Show subject-wise average marks")
        print("4. Show failed students (<20)")
        print("5. Show top 3 scorers")
        print("6. Exit")
        choice = input("Enter your choice: ")
        log_message(f"🧑🏻 User chose option '{choice}'")

        if choice == "1":
            show_all_students()
        elif choice == "2":
            show_sorted_students()
        elif choice == "3":
            show_subjectwise_average()
        elif choice == "4":
            show_failed_students()
        elif choice == "5":
            show_top_score()
        elif choice == "6":
            print("\n👋 Exiting....")
            log_message("❌ Program terminated by user")
            break
        else:
            print("\n 🤔 Invalid choice. Please choose a valid option.")
            log_message(f"'{choice}' is not a valid choice")
except FileNotFoundError:
    print("\n Error: The file 'student_data.csv' was not found.")
    log_message(" Error: The file 'student_data.csv' was not found.")
