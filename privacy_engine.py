"""Privacy engine for LGPD-oriented data sanitization."""
import re
import pandas as pd
from semantic_rules import CONTENT_RULES

SENSITIVE_TYPE_PLACEHOLDERS = {"Email":"<EMAIL>","CPF":"<CPF>","CNPJ":"<CNPJ>","CEP":"<CEP>","Telefone":"<PHONE>"}
SENSITIVE_SEMANTIC_TYPES = {"Email","CPF","CNPJ","CEP","Telefone"}
INLINE_PATTERNS = [
 {"placeholder":"<EMAIL>","pattern":r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"},
 {"placeholder":"<CPF>","pattern":r"\d{3}\.\d{3}\.\d{3}-\d{2}"},
 {"placeholder":"<CNPJ>","pattern":r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"},
 {"placeholder":"<PHONE>","pattern":r"(\+?\d{1,3}\s?)?\(?\d{2}\)?\s?\d{4,5}-?\d{4}"},
 {"placeholder":"<CEP>","pattern":r"(?<!\d)\d{5}-\d{3}(?!\d)"},
]
def _sanitize_value(value: str) -> str:
    result=value
    for rule in INLINE_PATTERNS: result=re.sub(rule["pattern"],rule["placeholder"],result)
    return result
def _sanitize_list(items: list) -> list:
    sanitized=[]
    for item in items:
        if isinstance(item,str): sanitized.append(_sanitize_value(item))
        elif isinstance(item,dict): sanitized.append(_sanitize_dict(item))
        elif isinstance(item,list): sanitized.append(_sanitize_list(item))
        else: sanitized.append(item)
    return sanitized
def _sanitize_dict(data: dict) -> dict:
    sanitized={}
    for key,value in data.items():
        if isinstance(value,str): sanitized[key]=_sanitize_value(value)
        elif isinstance(value,dict): sanitized[key]=_sanitize_dict(value)
        elif isinstance(value,list): sanitized[key]=_sanitize_list(value)
        else: sanitized[key]=value
    return sanitized
def sanitize_context(context: dict) -> dict:
    return _sanitize_dict(context)
def identify_sensitive_columns(df: pd.DataFrame) -> dict[str,str]:
    from semantic_engine import infer_semantic_type,infer_semantic_type_by_content,resolve_semantic_status
    sensitive_cols={}
    for col in df.columns:
        type_by_name=infer_semantic_type(col); type_by_content=infer_semantic_type_by_content(df[col])
        final_type,_=resolve_semantic_status(type_by_name,type_by_content)
        if final_type in SENSITIVE_SEMANTIC_TYPES: sensitive_cols[col]=SENSITIVE_TYPE_PLACEHOLDERS.get(final_type,"<REDACTED>")
    return sensitive_cols
def sanitize_dataframe_for_display(df: pd.DataFrame) -> pd.DataFrame:
    sensitive_cols=identify_sensitive_columns(df)
    if not sensitive_cols: return df
    sanitized=df.copy()
    for col,placeholder in sensitive_cols.items():
        if col in sanitized.columns:
            mask=sanitized[col].notna(); sanitized.loc[mask,col]=placeholder
    return sanitized
