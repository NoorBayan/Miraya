import json
import os

CONFIDENCE_THRESHOLD = 0.85
HITL_QUEUE_FILE = "data/hitl_queue.json"

def route_assertion(candidate_json: dict, validation_result: dict) -> str:
    """
    Routes the extracted semantics based on confidence calibration and validation logic,
    implementing the Human-in-the-Loop active learning mechanism (Section 5.4).
    """
    confidence = float(candidate_json.get("confidence_score", 0.0))
    review_flags = candidate_json.get("review_flags", [])
    
    if validation_result["status"] == "Rejected":
        return "Rejected"
        
    if validation_result["status"] == "Contradicted" or confidence < CONFIDENCE_THRESHOLD or len(review_flags) > 0:
        candidate_json["validation_notes"] = validation_result["log"]
        _save_to_hitl_queue(candidate_json)
        return "HITL_Queue"
        
    return "Accepted"

def _save_to_hitl_queue(data: dict):
    """
    Persists flagged annotations for expert adjudication.
    """
    os.makedirs(os.path.dirname(HITL_QUEUE_FILE), exist_ok=True)
    
    queue_data = []
    if os.path.exists(HITL_QUEUE_FILE):
        with open(HITL_QUEUE_FILE, "r", encoding="utf-8") as file:
            try:
                queue_data = json.load(file)
            except json.JSONDecodeError:
                queue_data = []
                
    queue_data.append(data)
    
    with open(HITL_QUEUE_FILE, "w", encoding="utf-8") as file:
        json.dump(queue_data, file, ensure_ascii=False, indent=4)
