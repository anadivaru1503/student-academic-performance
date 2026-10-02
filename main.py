import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folders
DATA_DIR = Path("data")
GRAPH_DIR = Path("graphs")
GRAPH_DIR.mkdir(exist_ok=True)

# Load Mathematics dataset
df = pd.read_csv(
    DATA_DIR / "student-mat.csv",
    sep=";"
)

# 1. Dataset overview
print("Dataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

# 2. Data types
print("\nData Types:")
print(df.dtypes)

# 3. Data quality assessment
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# 4. Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 5. Univariate analysis
plt.figure(figsize=(8, 5))
sns.histplot(df["G3"], bins=11, kde=True)
plt.title("Distribution of Final Grades")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "grade_distribution.png")
plt.show()

# 6. Bivariate analysis
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="studytime", y="G3")
plt.title("Study Time vs Final Grade")
plt.xlabel("Weekly Study Time")
plt.ylabel("Final Grade (G3)")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "studytime_vs_grade.png")
plt.show()

# 7. Grouping and aggregation
print("\nAverage Grade by Study Time:")
print(df.groupby("studytime")["G3"].mean())

# 8. Correlation analysis
grade_corr = df[["G1", "G2", "G3"]].corr()
print("\nGrade Correlation:")
print(grade_corr)

plt.figure(figsize=(7, 5))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(GRAPH_DIR / "correlation_heatmap.png")
plt.show()

print("\nAnalysis completed successfully!")