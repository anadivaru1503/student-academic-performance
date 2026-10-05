from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
GRAPH_DIR = ROOT / "graphs"
TABLE_DIR = ROOT / "tables"

GRAPH_DIR.mkdir(exist_ok=True)
TABLE_DIR.mkdir(exist_ok=True)

def load_math():
    return pd.read_csv(DATA_DIR / "student-mat.csv", sep=";")

def load_portuguese():
    return pd.read_csv(DATA_DIR / "student-por.csv", sep=";")

def save_table(df, filename):
    path = TABLE_DIR / filename
    df.to_csv(path, index=False)
    print(f"Saved table: {path}")
    return path

def save_fig(filename):
    path = GRAPH_DIR / filename
    plt.tight_layout()
    plt.savefig(path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Saved graph: {path}")
    return path

def clean_numeric(df, cols):
    return df[cols].apply(pd.to_numeric, errors="coerce")

sns.set_theme(style="whitegrid")
