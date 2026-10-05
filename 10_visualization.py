"""
Section 11: Visualization
"""
import pandas as pd
import matplotlib.pyplot as plt
from common import load_math, load_portuguese, save_table, save_fig

mat = load_math()
por = load_portuguese()

# Performance bands for Mathematics
bands = pd.cut(
    mat["G3"],
    bins=[-1, 9, 14, 20],
    labels=["Low (0-9)", "Medium (10-14)", "High (15-20)"]
)
band_counts = bands.value_counts().reindex(["Low (0-9)", "Medium (10-14)", "High (15-20)"]).reset_index()
band_counts.columns = ["Performance_Band", "Student_Count"]
save_table(band_counts, "15_performance_bands.csv")

plt.figure(figsize=(8, 5))
plt.bar(band_counts["Performance_Band"], band_counts["Student_Count"])
plt.title("Final-Grade Performance Bands")
plt.xlabel("Performance Band")
plt.ylabel("Number of Students")
save_fig("performance_bands.png")

# Mean G1, G2, G3
means = pd.DataFrame({
    "Grade": ["G1", "G2", "G3"],
    "Mean": [mat["G1"].mean(), mat["G2"].mean(), mat["G3"].mean()]
})
save_table(means, "16_mean_g1_g2_g3.csv")

plt.figure(figsize=(7, 5))
plt.bar(means["Grade"], means["Mean"])
plt.title("Mean G1, G2 and G3 - Mathematics")
plt.xlabel("Grade")
plt.ylabel("Mean Grade")
save_fig("mean_g1_g2_g3.png")

# Mathematics vs Portuguese final-grade means
comparison = pd.DataFrame({
    "Subject": ["Mathematics", "Portuguese"],
    "Mean_G3": [mat["G3"].mean(), por["G3"].mean()]
})
save_table(comparison, "17_math_vs_portuguese_g3.csv")

plt.figure(figsize=(7, 5))
plt.bar(comparison["Subject"], comparison["Mean_G3"])
plt.title("Mean Final Grade: Mathematics vs Portuguese")
plt.xlabel("Subject")
plt.ylabel("Mean G3")
save_fig("math_vs_portuguese_g3.png")
