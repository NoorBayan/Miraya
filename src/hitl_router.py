import json
import os
from typing import Dict, Any

HITL_QUEUE_PATH = "data/hitl_queue.json"

def _persist_to_adjudication_queue(data: Dict[str, Any]) -> None:
    """
    Safely commits borderline or contradicted assertions to the persistent queue
    for expert human review, ensuring data integrity.
    """
    os.makedirs(os.path.dirname(HITL_QUEUE_PATH), exist_ok=True)
    
    queue = []
    if os.path.exists(HITL_QUEUE_PATH):
        with open(HITL_QUEUE_PATH, "r", encoding="utf-8") as f:
            queue = json.load(f)
            
    queue.append(data)
    
    with open(HITL_QUEUE_PATH, "w", encoding="utf-8") as f:
        json.dump(queue, f, ensure_ascii=False, indent=4)

def route_assertion(candidate_json: Dict[str, Any], validation_result: Dict[str, Any]) -> str:
    """
    Determines the lifecycle path of extracted semantic tuples based on
    calibrated confidence and formal validation outcomes.
    """
    if validation_result["status"] == "Rejected":
        return "Rejected"
        
    confidence_level = candidate_json.get("confidence", "Low")
    review_flags = candidate_json.get("review_flags", [])
    
    if validation_result["status"] == "Contradicted" or confidence_level in ["Low", "Medium"] or len(review_flags) > 0:
        candidate_json["validation_provenance"] = validation_result["log"]
        _persist_to_adjudication_queue(candidate_json)
        return "HITL_Escalation"
        
    return "Graph_Commit"
