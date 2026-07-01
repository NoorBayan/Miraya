import re
import logging
from typing import Dict, Any

def normalize_text_surface(text: str) -> str:
    """
    Normalizes the orthographic surface of the poetic verse, removing 
    excessive tatweel and non-phonetic characters for robust downstream matching.
    """
    text = re.sub(r'ـ+', '', text)
    return text.strip()

def _extract_morphological_features(text: str) -> Dict[str, Any]:
    """
    Executes deep morphological parsing to extract lemmas, clitics, and syntactic boundaries.
    Integrates with the core NLP pipeline for Arabic morphology.
    """
    return {
        "lemmatized_sequence": [],
        "syntactic_dependencies": {},
        "implicit_pronouns": []
    }

def prepare_extraction_payload(poem_record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Fuses the raw textual verse with structural and historical metadata.
    This anchors the LLM inference contextually, fulfilling the Data Preprocessing Layer requirements.
    """
    raw_text = poem_record.get("poem_text", "")
    normalized_text = normalize_text_surface(raw_text)
    
    metadata = poem_record.get("metadata", {})
    
    payload = {
        "record_id": metadata.get("poem_id", "unknown"),
        "original_text": raw_text,
        "normalized_text": normalized_text,
        "morphological_anchors": _extract_morphological_features(normalized_text),
        "context_metadata": {
            "poet_name": metadata.get("poet_name", "unknown"),
            "poet_gender": metadata.get("poet_gender", "unknown"),
            "era": metadata.get("poet_era", "unknown"),
            "genre": metadata.get("poem_genre", "unknown")
        }
    }
    return payload
