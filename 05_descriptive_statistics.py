"""
Section 6: Descriptive Statistics
"""
import pandas as pd
from common import load_math, load_portuguese, save_table

mat = load_math()
por = load_portuguese()

cols = ["age", "studytime", "failures", "absences", "G1", "G2", "G3"]

summary = pd.DataFrame({
    "Mathematics_Mean": mat[cols].mean(),
    "Mathematics_Median": mat[cols].median(),
    "Mathematics_Std": mat[cols].std(),
    "Portuguese_Mean": por[cols].mean(),
    "Portuguese_Median": por[cols].median(),
    "Portuguese_Std": por[cols].std()
}).reset_index().rename(columns={"index": "Variable"})

print(summary.to_string(index=False))
save_table(summary, "04_descriptive_statistics.csv")

print("\nReported-document checkpoints:")
print(f"Mathematics G3 mean: {mat['G3'].mean():.2f}")
print(f"Portuguese G3 mean: {por['G3'].mean():.2f}")
