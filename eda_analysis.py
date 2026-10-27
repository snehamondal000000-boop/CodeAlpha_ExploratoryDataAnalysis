import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student-mat.csv", sep=";")

print("DATASET SHAPE")
print(df.shape)

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nDESCRIPTIVE STATISTICS")
print(df.describe())

print("\nAVERAGE FINAL GRADE:", round(df["G3"].mean(), 2))

print("\nAVERAGE FINAL GRADE BY STUDY TIME")
print(df.groupby("studytime")["G3"].mean().round(2))

print("\nAVERAGE FINAL GRADE BY PREVIOUS FAILURES")
print(df.groupby("failures")["G3"].mean().round(2))

print("\nAVERAGE FINAL GRADE BY GENDER")
print(df.groupby("sex")["G3"].mean().round(2))

print("\nAVERAGE FINAL GRADE BY INTERNET ACCESS")
print(df.groupby("internet")["G3"].mean().round(2))

print("\nCORRELATION WITH FINAL GRADE (G3)")
print(df.select_dtypes("number").corr()["G3"].sort_values(ascending=False))

# Visualizations
plt.figure(figsize=(8,5))
plt.hist(df["G3"], bins=11)
plt.title("Distribution of Final Grades (G3)")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("grade_distribution.png")
plt.show()

plt.figure(figsize=(8,5))
df.groupby("studytime")["G3"].mean().plot(kind="bar")
plt.title("Average Final Grade by Study Time")
plt.xlabel("Study Time Category")
plt.ylabel("Average G3")
plt.tight_layout()
plt.savefig("studytime_vs_grade.png")
plt.show()

plt.figure(figsize=(8,5))
df.groupby("failures")["G3"].mean().plot(kind="bar")
plt.title("Average Final Grade by Previous Failures")
plt.xlabel("Previous Failures")
plt.ylabel("Average G3")
plt.tight_layout()
plt.savefig("failures_vs_grade.png")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["absences"], df["G3"], alpha=0.6)
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig("absences_vs_grade.png")
plt.show()
