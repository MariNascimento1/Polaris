"""Descriptive statistics calculations."""
import pandas as pd
import numpy as np

def format_br(value, decimals: int = 2, prefix: str = "") -> str:
    """Format a number using Brazilian convention (dot for thousands, comma for decimal)."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "N/A"
    formatted = f"{value:,.{decimals}f}"
    formatted = formatted.replace(",", "@").replace(".", ",").replace("@", ".")
    return f"{prefix}{formatted}"

def compute_numeric_statistics(df: pd.DataFrame, columns: list[str] | None = None, monetary_columns: list[str] | None = None) -> pd.DataFrame | None:
    numeric_df = df[columns].select_dtypes(include="number") if columns is not None else df.select_dtypes(include="number")
    if numeric_df.empty:
        return None
    money_set = set(monetary_columns or [])
    rows = []
    for col in numeric_df.columns:
        series = numeric_df[col].dropna()
        if series.empty:
            continue
        prefix = "R$ " if col in money_set else ""
        rows.append({"Coluna": col, "Média": format_br(series.mean(), prefix=prefix), "Mediana": format_br(series.median(), prefix=prefix), "Mínimo": format_br(series.min(), prefix=prefix), "Máximo": format_br(series.max(), prefix=prefix), "Desvio Padrão": format_br(series.std(), prefix=prefix)})
    return pd.DataFrame(rows) if rows else None

def compute_categorical_statistics(df: pd.DataFrame) -> pd.DataFrame | None:
    categorical_df = df.select_dtypes(include=["object", "category"])
    if categorical_df.empty:
        return None
    rows = []
    for col in categorical_df.columns:
        mode_value = categorical_df[col].mode()
        most_frequent = mode_value.iloc[0] if not mode_value.empty else None
        frequency = int(categorical_df[col].value_counts().iloc[0]) if most_frequent is not None else 0
        rows.append({"Coluna": col, "Valores Únicos": categorical_df[col].nunique(), "Valor Mais Frequente": most_frequent, "Frequência": frequency})
    return pd.DataFrame(rows)

def compute_advanced_numeric_statistics(df: pd.DataFrame) -> list[dict] | None:
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        return None
    results = []
    for col in numeric_df.columns:
        series = numeric_df[col].dropna()
        if series.empty:
            results.append({"column": col, "mean": None}); continue
        q1=float(series.quantile(.25)); q3=float(series.quantile(.75)); iqr=q3-q1
        outlier_count=int(((series < q1-1.5*iqr) | (series > q3+1.5*iqr)).sum())
        mode_values=series.mode(); mode=float(mode_values.iloc[0]) if not mode_values.empty else None
        results.append({"column":col,"mean":float(series.mean()),"median":float(series.median()),"mode":mode,"min":float(series.min()),"max":float(series.max()),"std":float(series.std()),"q1":q1,"q3":q3,"iqr":iqr,"outlier_count":outlier_count,"skewness":float(series.skew())})
    return results

def compute_advanced_categorical_statistics(df: pd.DataFrame) -> list[dict] | None:
    categorical_df=df.select_dtypes(include=["object","category"])
    if categorical_df.empty: return None
    results=[]
    for col in categorical_df.columns:
        series=categorical_df[col].dropna(); total=len(series); value_counts=series.value_counts()
        top_5=[{"value":str(k),"count":int(v),"percentage":round(v/total*100,2) if total>0 else 0.0} for k,v in value_counts.head(5).items()]
        dominant_pct=round(float(value_counts.iloc[0])/total*100,2) if total>0 and not value_counts.empty else 0.0
        results.append({"column":col,"cardinality":int(series.nunique()),"dominant_category":str(value_counts.index[0]) if not value_counts.empty else None,"dominant_percentage":dominant_pct,"top_5":top_5})
    return results
