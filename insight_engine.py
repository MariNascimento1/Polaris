"""Deterministic insight generation based on data quality, statistics, and semantics."""
import pandas as pd
from quality import compute_data_quality_summary, compute_missing_values, compute_unique_values
from statistics import compute_numeric_statistics, compute_categorical_statistics
from semantic_engine import infer_semantic_type, infer_semantic_type_by_content, resolve_semantic_status

def _generate_quality_insights(df: pd.DataFrame) -> list[str]:
    insights=[]; summary=compute_data_quality_summary(df)
    if summary["total_duplicates"]==0: insights.append("Nenhuma linha duplicada foi encontrada.")
    else: insights.append(f"Foram encontradas {summary['total_duplicates']} linhas duplicadas ({summary['pct_duplicates']:.1f}% do dataset).")
    missing_df=compute_missing_values(df); total_missing=int(missing_df["Valores Ausentes"].sum())
    if total_missing==0: insights.append("O dataset não possui valores ausentes.")
    else:
        cols_with_missing=int((missing_df["Valores Ausentes"]>0).sum())
        insights.append(f"Existem valores ausentes em {cols_with_missing} coluna(s), totalizando {total_missing} valores faltantes.")
    if summary["pct_complete"]>=90 and summary["pct_duplicates"]<=5: insights.append("O dataset apresenta boa qualidade para análise.")
    elif summary["pct_complete"]<50: insights.append("O dataset possui muitos dados faltantes, o que pode comprometer análises.")
    return insights

def _generate_statistics_insights(df: pd.DataFrame) -> list[str]:
    insights=[]
    for col in df.columns:
        unique_vals=df[col].dropna().unique()
        if len(unique_vals)==2:
            sorted_vals=sorted([str(v).lower() for v in unique_vals])
            boolean_pairs=[["0","1"],["false","true"],["n","s"],["nao","sim"],["no","yes"],["não","sim"]]
            if sorted_vals in boolean_pairs: insights.append(f'A coluna "{col}" é booleana.')
    unique_df=compute_unique_values(df); total_rows=len(df)
    for _,row in unique_df.iterrows():
        if total_rows>0 and row["Valores Únicos"]==total_rows: insights.append(f'A coluna "{row["Coluna"]}" possui valores completamente únicos.')
    return insights

def _generate_semantic_insights(df: pd.DataFrame) -> list[str]:
    insights=[]; semantic_types=[]
    for col in df.columns:
        type_by_name=infer_semantic_type(col); type_by_content=infer_semantic_type_by_content(df[col])
        final_type,_=resolve_semantic_status(type_by_name,type_by_content); semantic_types.append(final_type)
    unique_types=set(semantic_types)
    has_lat="Latitude" in unique_types; has_lon="Longitude" in unique_types
    if has_lat and has_lon:
        insights.extend(["Foram detectadas coordenadas geográficas (latitude e longitude).","O dataset parece conter informações geográficas."])
    elif has_lat or has_lon: insights.append("O dataset parece conter informações geográficas parciais.")
    for label,message in [("Email","O dataset contém endereços de e-mail."),("CPF","Foram detectados números de CPF no dataset."),("CNPJ","Foram detectados números de CNPJ no dataset."),("CEP","Foram detectados CEPs no dataset."),("Moeda / Valor","O dataset contém colunas com valores monetários."),("Data","O dataset contém colunas de data/tempo.")]:
        if label in unique_types: insights.append(message)
    return insights

def generate_insights(df: pd.DataFrame) -> list[str]:
    insights=[]; insights.extend(_generate_quality_insights(df)); insights.extend(_generate_statistics_insights(df)); insights.extend(_generate_semantic_insights(df)); return insights
