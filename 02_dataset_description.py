"""
Section 2: Dataset Description
"""
import pandas as pd
from common import load_math, load_portuguese, save_table

mat = load_math()
por = load_portuguese()

summary = pd.DataFrame([
    ["Mathematics", len(mat), mat.shape[1]],
    ["Portuguese", len(por), por.shape[1]],
    ["Combined", len(mat) + len(por), mat.shape[1]],
], columns=["Subject", "Records", "Attributes"])

print(summary.to_string(index=False))
save_table(summary, "01_dataset_summary.csv")
