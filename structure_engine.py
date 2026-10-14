"""Data structure detection engine."""

import pandas as pd


def detect_primary_keys(df: pd.DataFrame) -> list[str]:
    return [col for col in df.columns if df[col].isnull().sum() == 0 and df[col].nunique() == len(df)]


def detect_constant_columns(df: pd.DataFrame) -> list[str]:
    return [col for col in df.columns if df[col].dropna().nunique() == 1]


def detect_boolean_columns(df: pd.DataFrame) -> list[str]:
    return [col for col in df.columns if df[col].dropna().nunique() == 2]


def detect_low_cardinality_columns(df: pd.DataFrame) -> list[str]:
    low_card, total_rows = [], len(df)
    for col in df.columns:
        n_unique = df[col].dropna().nunique()
        if n_unique < 10 or (total_rows > 0 and (n_unique / total_rows) < 0.05):
            low_card.append(col)
    return low_card


def detect_fully_unique_columns(df: pd.DataFrame) -> list[str]:
    unique_cols = []
    for col in df.columns:
        non_null = df[col].dropna()
        if len(non_null) > 0 and non_null.nunique() == len(non_null):
            unique_cols.append(col)
    return unique_cols


def analyze_structure(df: pd.DataFrame) -> dict:
    return {"primary_keys": detect_primary_keys(df), "constant_columns": detect_constant_columns(df), "boolean_columns": detect_boolean_columns(df), "low_cardinality_columns": detect_low_cardinality_columns(df), "fully_unique_columns": detect_fully_unique_columns(df)}
