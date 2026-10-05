"""
Sections 4 and 5: Tools Used for Analysis + Data Quality Assessment
"""
import pandas as pd
from common import load_math, load_portuguese, save_table

mat = load_math()
por = load_portuguese()

quality = pd.DataFrame([
    ["Mathematics", len(mat), int(mat.isna().sum().sum()), int(mat.duplicated().sum()),
     mat["G3"].min(), mat["G3"].max(), mat["age"].min(), mat["age"].max(), mat["absences"].mean(), mat["absences"].max()],
    ["Portuguese", len(por), int(por.isna().sum().sum()), int(por.duplicated().sum()),
     por["G3"].min(), por["G3"].max(), por["age"].min(), por["age"].max(), por["absences"].mean(), por["absences"].max()]
], columns=[
    "Subject","Records","Missing_Cells","Duplicate_Rows",
    "G3_Min","G3_Max","Age_Min","Age_Max","Mean_Absences","Max_Absences"
])

print(quality.to_string(index=False))
save_table(quality, "03_data_quality_assessment.csv")

print("\nTools used: Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter/VS Code, Git and GitHub.")
