"""Data quality calculations."""

import pandas as pd


def compute_data_quality_summary(df: pd.DataFrame) -> dict:
    total_rows = len(df)
    total_duplicates = int(df.duplicated().sum())
    pct_duplicates = (total_duplicates / total_rows * 100) if total_rows > 0 else 0.0
    complete_rows = int(df.dropna().shape[0])
    pct_complete = (complete_rows / total_rows * 100) if total_rows > 0 else 0.0
    memory_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
    return {"total_duplicates": total_duplicates, "pct_duplicates": pct_duplicates, "complete_rows": complete_rows, "pct_complete": pct_complete, "memory_mb": memory_mb}


def compute_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    missing = df.isnull().sum()
    return pd.DataFrame({"Coluna": missing.index, "Valores Ausentes": missing.values})


def compute_unique_values(df: pd.DataFrame) -> pd.DataFrame:
    unique_counts = df.nunique()
    return pd.DataFrame({"Coluna": unique_counts.index, "Valores Únicos": unique_counts.values})
