"""
Section 8: Bivariate Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
from common import load_math, save_table, save_fig

df = load_math()

# Previous failures vs final grade
fail_group = df.groupby("failures", as_index=False)["G3"].mean()
fail_group.columns = ["Previous_Failures", "Mean_G3"]
save_table(fail_group, "06_failures_vs_g3.csv")

plt.figure(figsize=(8, 5))
plt.bar(fail_group["Previous_Failures"].astype(str), fail_group["Mean_G3"])
plt.title("Previous Failures vs Mean Final Grade")
plt.xlabel("Previous Failures")
plt.ylabel("Mean G3")
save_fig("failures_vs_g3.png")

# Study time vs final grade
study_group = df.groupby("studytime", as_index=False)["G3"].mean()
study_group.columns = ["Study_Time_Code", "Mean_G3"]
save_table(study_group, "07_studytime_vs_g3.csv")

plt.figure(figsize=(8, 5))
plt.plot(study_group["Study_Time_Code"], study_group["Mean_G3"], marker="o")
plt.title("Study Time vs Mean Final Grade")
plt.xlabel("Study Time Category")
plt.ylabel("Mean G3")
save_fig("studytime_vs_g3.png")

# G2 vs G3 scatter
plt.figure(figsize=(7, 5))
plt.scatter(df["G2"], df["G3"], alpha=0.65)
plt.title("Second-Period Grade (G2) vs Final Grade (G3)")
plt.xlabel("G2")
plt.ylabel("G3")
save_fig("g2_vs_g3_scatter.png")

print("G2-G3 correlation:", df["G2"].corr(df["G3"]))
print("G1-G3 correlation:", df["G1"].corr(df["G3"]))
