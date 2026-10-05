"""
Section 3: Data Types and Variables
"""
import pandas as pd
from common import load_math, save_table

df = load_math()

rows = []
for col in df.columns:
    rows.append({
        "Variable": col,
        "Data_Type": str(df[col].dtype),
        "Unique_Values": df[col].nunique(),
        "Missing_Values": int(df[col].isna().sum())
    })

table = pd.DataFrame(rows)
print(table.to_string(index=False))
save_table(table, "02_variable_data_types.csv")

print("\nMain academic variables: G1, G2, G3")
print("G3 is treated as the main final-grade target.")
