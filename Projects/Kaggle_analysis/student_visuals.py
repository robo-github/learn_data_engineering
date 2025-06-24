import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set Seaborn style
sns.set(style="whitegrid")

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Group by gender and calculate average math score
avg_math_by_gender = df.groupby("gender")["math_score"].mean().reset_index()

# Plot the bar chart
plt.figure(figsize=(6, 4))
sns.barplot(data=avg_math_by_gender, x="gender",
            y="math_score", palette="Set2")
plt.title("Average Math Score by Gender")
plt.ylabel("Math Score")
plt.xlabel("Gender")
plt.tight_layout()
plt.show()
