import pandas as pd

# Create a DataFrame
df = pd.read_csv("StudentsPerformance.csv")

# Print the first 5 rows of the DataFrame
print(df.head())

# show column info
print("\n📌Data info: ")
print(df.info())

# show numbers of rows and columns
print("Shape of the dataSet: ", df.shape)

# Clean column names: lowercase and replace spaces with underscores
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Show updated columns names
print("\n📋 Cleaned Column Names:")
print(df.columns)


# Step 1: Basic statistics for all scores
print("\n📊 Basic Statistics for all Scores:")
print(df[["math_score", "reading_score", "writing_score"]].describe())

# Step 2: Average marks per subject
print("\n📊 Average Score:")
print("Maths: ", df["math_score"].mean())
print("Reading: ", df["reading_score"].mean())
print("Writing: ", df["writing_score"].mean())


# ------------------------------Data Cleaned-----------------------------------#

# Group the students by gender and calculate average scores
average_score_by_gender = df.groupby(
    "gender")[["math_score", "reading_score", "writing_score"]].mean()
print("\n📊 Average Score By Gender: ")
print(average_score_by_gender)

# students who completed the test preparation course and scored above 85 in math
high_achiever = df[(df["test_preparation_course"] ==
                    "completed") & (df["math_score"] > 85)]
print("\n📊 High Achievers: ")
print(high_achiever)

# Count the students completed or None in test preparation course
count_of_test_preparation = df.groupby("test_preparation_course")[
    "math_score"].count()
print("\n📊 Test Preparation Course Count: ")
print(count_of_test_preparation)

# Compare average scores by gender and lunch type
avg_by_gender_lunch = df.groupby(["gender", "lunch"])[
    ["math_score", "reading_score", "writing_score"]].mean()
print("\n📊 Average Score By Gender and Lunch Type: ")
print(avg_by_gender_lunch)

# Show top score
print("\n📊 Top Score: ")
