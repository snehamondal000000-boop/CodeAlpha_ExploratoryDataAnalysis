# CodeAlpha — Exploratory Data Analysis

## Student Performance Dataset

### Objective
This project performs Exploratory Data Analysis (EDA) on the UCI Student Performance dataset to identify patterns related to students' final mathematics grades.

### Dataset
- Dataset: Student Performance
- File used: `student-mat.csv`
- Records: 395 students
- Target/analysis column: `G3` (final grade, 0–20)

### Questions
1. What is the distribution of final grades?
2. Does study time relate to final grade?
3. How do previous failures relate to performance?
4. Is there a relationship between absences and final grade?
5. How does average performance differ by gender and internet access?

### Analysis performed
- Dataset shape and structure
- Data types
- Missing-value check
- Duplicate-value check
- Descriptive statistics
- Grouped analysis
- Correlation analysis
- Data visualization

### Visualizations
- Final grade distribution
- Study time vs average final grade
- Previous failures vs average final grade
- Absences vs final grade

### Tools
Python, Pandas, Matplotlib

### Dataset source
UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/320/student+performance

### Note
The dataset is publicly available from the UCI Machine Learning Repository. `G1` and `G2` are earlier grades and are strongly related to `G3`, so their correlation should not be interpreted as proof of causation.
