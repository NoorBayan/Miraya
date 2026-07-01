import logging
from typing import Dict, Any

from src.preprocessing import prepare_extraction_payload
from src.prompt_engine import build_ontology_prompt
from src.llm_inference import run_ontology_inference
from src.constraint_validator import validate_candidate_graph
from src.hitl_router import route_assertion
from src.kg_serializer import serialize_to_rdf

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def execute_extraction_pipeline(raw_record: Dict[str, Any]) -> None:
    """
    Main Orchestrator: Drives the end-to-end neuro-symbolic extraction process.
    """
    record_id = raw_record.get("metadata", {}).get("poem_id", "Unknown")
    logging.info(f"Initiating pipeline for Poetic Unit: {record_id}")
    
    # Phase 1: Semantic Anchoring & Preprocessing
    payload = prepare_extraction_payload(raw_record)
    
    # Phase 2: Ontology-Guided Inference
    prompt = build_ontology_prompt()
    candidate_assertion = run_ontology_inference(payload, prompt)
    
    # Phase 3: Formal Constraint Validation
    validation_state = validate_candidate_graph(candidate_assertion)
    
    # Phase 4: Lifecycle Routing (HITL vs Accept)
    routing_path = route_assertion(candidate_assertion, validation_state)
    logging.info(f"Routing Decision: {routing_path} | Status: {validation_state['status']}")
    
    # Phase 5: Knowledge Graph Serialization
    if routing_path == "Graph_Commit":
        rdf_triples = serialize_to_rdf(candidate_assertion)
        logging.info("Successfully integrated semantic tuple into Knowledge Graph.")
    else:
        logging.info("Serialization bypassed; assertion escalated to HITL framework.")

if __name__ == "__main__":
    # Execution entry point for the batch processing engine
    sample_verse_data = {
        "metadata": {
            "poem_id": "P_704",
            "poet_name": "لبيد بن ربيعة العامري",
            "poet_gender": "Male",
            "poet_era": "Pre-Islamic",
            "poem_genre": "Fakhr"
        },
        "poem_text": "سَعَى خُزَيْمَةُ فِي قَوْم لِيُهْلِكَهُمْ *** لَى الْحَمَّالَةِ هَلْ بِالْمَرْءِ مِنْ كَلْب"
    }
    
    execute_extraction_pipeline(sample_verse_data)
