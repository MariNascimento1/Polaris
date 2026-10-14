"""Semantic detection rules for column profiling."""

SEMANTIC_RULES = [
    {"label": "Data", "pattern": r"\b(date|data|datetime|timestamp|time|dia|mes|ano|year|month|day|created_at|updated_at)\b"},
    {"label": "Email", "pattern": r"\b(email|e-mail|correo)\b"},
    {"label": "Telefone", "pattern": r"\b(telefone|phone|celular|cel|fone|mobile|whatsapp)\b"},
    {"label": "Latitude", "pattern": r"\b(lat|latitude)\b"},
    {"label": "Longitude", "pattern": r"\b(lon|lng|long|longitude)\b"},
    {"label": "Moeda / Valor", "pattern": r"price|preco|valor|cost|custo|revenue|receita|salary|salario|amount|total_gasto|ticket_medio|gasto|faturamento"},
    {"label": "Identificador (ID)", "pattern": r"\bid\b|_id\b|^id_|^cod_|^codigo|^code|protocolo|^numero_id|^numero_ref"},
]
CONTENT_RULES = [
    {"label": "Email", "pattern": r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"},
    {"label": "Data", "pattern": r"^\d{4}[-/]\d{1,2}[-/]\d{1,2}$|^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}$|^\d{1,2}\s+(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez|jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\s+\d{2,4}$"},
    {"label": "CPF", "pattern": r"^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$"},
    {"label": "CNPJ", "pattern": r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$|^\d{14}$"},
    {"label": "CEP", "pattern": r"^\d{5}-?\d{3}$"},
    {"label": "Telefone", "pattern": r"^(\+?\d{1,3}\s?)?\(?\d{2}\)?\s?\d{4,5}-?\d{4}$"},
    {"label": "Latitude", "pattern": r"^-?([0-8]?\d(\.\d+)?|90(\.0+)?)$"},
    {"label": "Longitude", "pattern": r"^-?(1[0-7]\d(\.\d+)?|0?\d{1,2}(\.\d+)?|180(\.0+)?)$"},
]
CONTENT_SAMPLE_SIZE = 100
CONTENT_MATCH_THRESHOLD = 0.5
