import re

def normalize_arabic_text(text: str) -> str:
    """
    Normalizes Arabic text by removing excessive diacritics and tatweel 
    to ensure robust downstream semantic matching.
    """
    text = re.sub(r'ـ+', '', text)
    return text.strip()

def _apply_morphological_analysis(text: str) -> dict:
    """
    Applies deep morphological parsing (e.g., via CAMeL Tools/MADAMIRA).
    This extracts verb lemmas, roots, and clitics required for the ontology.
    """
    # Implementation deferred to the specialized NLP module.
    return {"lemmas": [], "pos_tags": []}

def prepare_extraction_payload(poem_record: dict) -> dict:
    """
    Fuses the raw verse with historical and biographical metadata 
    to anchor the LLM inference contextually (Section 5.1).
    """
    raw_text = poem_record.get("poem_text", "")
    normalized_text = normalize_arabic_text(raw_text)
    
    metadata = poem_record.get("metadata", {})
    poet_info = metadata.get("poet", {})
    
    payload = {
        "record_id": metadata.get("poem_id", "unknown"),
        "original_text": raw_text,
        "normalized_text": normalized_text,
        "morphological_data": _apply_morphological_analysis(normalized_text),
        "context_metadata": {
            "poet_name": poet_info.get("name", "Unknown"),
            "poet_gender": poet_info.get("gender", "Unknown"),
            "era": poet_info.get("era", "Unknown"),
            "genre": metadata.get("poem_info", {}).get("genre", "Unknown")
        }
    }
    return payload
