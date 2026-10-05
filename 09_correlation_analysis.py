"""
Section 10: Correlation Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import load_math, save_table, save_fig

df = load_math()

numeric_cols = [
    "age", "Medu", "Fedu", "traveltime", "studytime",
    "failures", "famrel", "freetime", "goout",
    "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"
]

corr = df[numeric_cols].corr()
save_table(corr.reset_index().rename(columns={"index": "Variable"}), "13_correlation_matrix.csv")

g3_corr = corr["G3"].sort_values(ascending=False).reset_index()
g3_corr.columns = ["Variable", "Correlation_with_G3"]
save_table(g3_corr, "14_correlations_with_g3.csv")

plt.figure(figsize=(11, 9))
sns.heatmap(corr, cmap="coolwarm", center=0, annot=False)
plt.title("Correlation Heatmap - Mathematics Dataset")
save_fig("correlation_heatmap.png")

print(g3_corr.to_string(index=False))
