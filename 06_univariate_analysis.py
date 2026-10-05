"""
Section 7: Univariate Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
from common import load_math, save_table, save_fig

df = load_math()

# Table: selected categorical distributions
categorical_cols = ["sex", "school", "address", "higher", "internet", "Pstatus"]
rows = []
for col in categorical_cols:
    counts = df[col].value_counts(dropna=False)
    for category, count in counts.items():
        rows.append([col, category, int(count), float(count / len(df) * 100)])

dist = pd.DataFrame(rows, columns=["Variable", "Category", "Count", "Percentage"])
save_table(dist, "05_univariate_distributions.csv")
print(dist.to_string(index=False))

# Graph 1: Final-grade distribution
plt.figure(figsize=(8, 5))
plt.hist(df["G3"], bins=21, edgecolor="black")
plt.title("Distribution of Final Mathematics Grades (G3)")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Number of Students")
save_fig("g3_distribution.png")

# Graph 2: Gender composition
gender = df["sex"].value_counts()
plt.figure(figsize=(6, 5))
plt.bar(gender.index.astype(str), gender.values)
plt.title("Students by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
save_fig("gender_distribution.png")
