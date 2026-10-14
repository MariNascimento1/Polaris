"""Domain detection rules for dataset context inference."""

DOMAIN_RULES = [
    {"domain": "Geográfico", "required": ["Latitude", "Longitude"], "optional": ["CEP", "Identificador (ID)"]},
    {"domain": "Financeiro", "required": ["Moeda / Valor"], "optional": ["Data", "Identificador (ID)"]},
    {"domain": "Cadastro de Pessoas", "required": ["CPF"], "optional": ["Email", "Data", "Identificador (ID)", "CEP"]},
    {"domain": "Cadastro Empresarial", "required": ["CNPJ"], "optional": ["Email", "Data", "Identificador (ID)", "CEP", "Moeda / Valor"]},
    {"domain": "Comunicação", "required": ["Email"], "optional": ["Data", "Identificador (ID)"]},
    {"domain": "Temporal", "required": ["Data"], "optional": ["Identificador (ID)", "Moeda / Valor"]},
]
