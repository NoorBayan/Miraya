def validate_candidate_graph(candidate_json: dict) -> dict:
    """
    Executes Algorithm 1: Deterministic Constraint Validation & Routing.
    Evaluates candidate assertions against ontological SHACL constraints and logical rules.
    """
    validation_log = []
    is_valid = True
    
    if candidate_json.get("status") == "Error":
        return {"status": "Rejected", "log": ["JSON Parsing Failure."]}

    # 1. Structural Conformance (Schema Validation)
    required_fields = ["main_event", "participants", "confidence_score"]
    for field in required_fields:
        if field not in candidate_json:
            validation_log.append(f"Fatal Violation: Missing mandatory property '{field}' (C03).")
            is_valid = False
            return {"status": "Rejected", "log": validation_log}
            
    # 2. Semantic Integrity Rules (SHACL-SPARQL Logic Equivalent)
    man_roles = candidate_json.get("man_roles_all", [])
    woman_roles = candidate_json.get("woman_roles_all", [])
    all_roles = man_roles + woman_roles

    # Rule C01: Orphan agents without associated actions are disallowed
    if all_roles and not candidate_json.get("events"):
        validation_log.append("Contradiction (C01): Roles assigned without identifying any valid events.")
        is_valid = False

    # Rule C09: Check for mutual exclusion in Gaze Direction vs Participants
    gaze = candidate_json.get("gaze_direction")
    if gaze in ["Male-to-Female", "Female-to-Male"] and (not man_roles or not woman_roles):
        validation_log.append("Contradiction (C09): Gaze direction implies mixed genders, but participants are uniform.")
        is_valid = False

    if not is_valid:
        return {"status": "Contradicted", "log": validation_log}
        
    return {"status": "Valid", "log": ["All SHACL structural and logic constraints satisfied."]}
