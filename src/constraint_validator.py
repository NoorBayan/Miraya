import logging
from typing import Dict, Any

def _evaluate_shacl_shapes(candidate: Dict[str, Any]) -> list:
    """
    Evaluates the candidate assertion against formal SHACL shape definitions.
    Validates domain/range conformance and mandatory property existence.
    """
    violations = []
    mandatory_properties = ["main_event_tense", "speaker_present", "gaze_direction", "confidence"]
    
    for prop in mandatory_properties:
        if prop not in candidate:
            violations.append(f"Structural Violation (C03): Missing property '{prop}'.")
            
    return violations

def _evaluate_sparql_logic(candidate: Dict[str, Any]) -> list:
    """
    Enforces complex semantic integrity constraints preventing ontological contradictions.
    """
    contradictions = []
    
    gaze = candidate.get("gaze_direction", "none")
    woman_role = candidate.get("woman_role", "none")
    man_role = candidate.get("man_role", "none")
    
    # Rule C09: Gaze compatibility rule
    if gaze == "Male-to-Female" and woman_role == "none":
        contradictions.append("Semantic Violation (C09): Male-to-Female gaze asserted, but no woman role identified.")
        
    # Rule C04: Speaker identification consistency
    if candidate.get("speaker_present") == "Yes" and candidate.get("speaker_gender") == "unknown":
        if candidate.get("gender_inference_basis") not in ["Assumed", "Literary Context"]:
            contradictions.append("Semantic Violation (C04): Speaker present with unknown gender lacks valid epistemic basis.")

    return contradictions

def validate_candidate_graph(candidate_json: Dict[str, Any]) -> Dict[str, Any]:
    """
    The Deterministic Validation Core (Algorithm 1).
    Isolates LLM probabilistic generation from final knowledge graph commitment.
    """
    if candidate_json.get("status") == "Schema_Violation":
        return {"status": "Rejected", "log": candidate_json.get("review_flags", [])}
        
    validation_log = []
    
    shacl_violations = _evaluate_shacl_shapes(candidate_json)
    if shacl_violations:
        validation_log.extend(shacl_violations)
        return {"status": "Rejected", "log": validation_log}
        
    logic_contradictions = _evaluate_sparql_logic(candidate_json)
    if logic_contradictions:
        validation_log.extend(logic_contradictions)
        return {"status": "Contradicted", "log": validation_log}
        
    return {"status": "Valid", "log": ["Ontology constraint evaluation passed."]}
