"""
Section 9: Grouping and Aggregation
"""
import pandas as pd
import matplotlib.pyplot as plt
from common import load_math, save_table, save_fig

df = load_math()

# Study time grouping
study = df.groupby("studytime", as_index=False)["G3"].agg(["mean", "count"]).reset_index()
study.columns = ["Study_Time_Code", "Mean_G3", "Student_Count"]
save_table(study, "08_grouped_studytime.csv")

# Higher education intention
higher = df.groupby("higher", as_index=False)["G3"].agg(["mean", "count"]).reset_index()
higher.columns = ["Higher_Education_Intention", "Mean_G3", "Student_Count"]
save_table(higher, "09_grouped_higher_education.csv")

plt.figure(figsize=(7, 5))
plt.bar(higher["Higher_Education_Intention"].astype(str), higher["Mean_G3"])
plt.title("Higher-Education Intention vs Mean Final Grade")
plt.xlabel("Higher-Education Intention")
plt.ylabel("Mean G3")
save_fig("higher_education_vs_g3.png")

# Internet access
internet = df.groupby("internet", as_index=False)["G3"].mean()
internet.columns = ["Internet_Access", "Mean_G3"]
save_table(internet, "10_grouped_internet.csv")

# Urban/rural
address = df.groupby("address", as_index=False)["G3"].mean()
address.columns = ["Address_Type", "Mean_G3"]
save_table(address, "11_grouped_address.csv")

# Maternal education
medu = df.groupby("Medu", as_index=False)["G3"].mean()
medu.columns = ["Mother_Education_Code", "Mean_G3"]
save_table(medu, "12_grouped_maternal_education.csv")

print("\nStudy-time grouping:")
print(study.to_string(index=False))
