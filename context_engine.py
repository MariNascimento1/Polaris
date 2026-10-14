"""Context engine for dataset domain inference."""

from domain_rules import DOMAIN_RULES


def infer_domain(semantic_types: list[str]) -> dict:
    """Infer dataset domain from detected semantic types."""
    unique_types = set(semantic_types)
    best_match = {"domain": "Não Identificado", "confidence": 0.0, "matched_required": [], "matched_optional": []}
    for rule in DOMAIN_RULES:
        required, optional = rule["required"], rule["optional"]
        matched_required = [t for t in required if t in unique_types]
        matched_optional = [t for t in optional if t in unique_types]
        if len(matched_required) < len(required):
            continue
        required_score = 1.0
        optional_score = len(matched_optional) / len(optional) if optional else 1.0
        confidence = (required_score * 0.7) + (optional_score * 0.3)
        if confidence > best_match["confidence"]:
            best_match = {"domain": rule["domain"], "confidence": round(confidence, 2), "matched_required": matched_required, "matched_optional": matched_optional}
    return best_match
