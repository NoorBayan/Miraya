import logging
from src.preprocessing import prepare_extraction_payload
from src.prompt_engine import build_ontology_prompt
from src.llm_inference import run_llm_inference
from src.constraint_validator import validate_candidate_graph
from src.hitl_router import route_assertion
from src.kg_serializer import serialize_to_rdf

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_poem_record(raw_record: dict):
    """
    The Orchestrator: Executes the Constraint-Guided Semantic Extraction Architecture.
    """
    record_id = raw_record.get('metadata', {}).get('poem_id', 'Unknown')
    logging.info(f"Initiating pipeline for Record ID: {record_id}")
    
    # Layer 1: Data Preprocessing
    payload = prepare_extraction_payload(raw_record)
    logging.info("Layer 1 Complete: Data Preprocessed and Anchored.")
    
    # Layer 2: Ontology-Guided Inference
    prompt = build_ontology_prompt()
    candidate_json = run_llm_inference(payload, prompt)
    logging.info("Layer 2 Complete: Candidate Semantics Generated.")
    
    # Layer 3: Deterministic Constraint Validation
    validation_result = validate_candidate_graph(candidate_json)
    logging.info(f"Layer 3 Complete: Validation Status - {validation_result['status']}")
    
    # Layer 4: Human-in-the-Loop Routing
    routing_decision = route_assertion(candidate_json, validation_result)
    logging.info(f"Layer 4 Complete: Routing Decision - {routing_decision}")
    
    # Layer 5: Knowledge Graph Serialization
    if routing_decision == "Accepted":
        rdf_output = serialize_to_rdf(candidate_json)
        logging.info("Layer 5 Complete: Semantic assertions committed to Knowledge Graph.")
        # Logic to save the RDF string to triple-store or file goes here.
    else:
        logging.warning("Serialization skipped due to HITL diversion or rejection.")

if __name__ == "__main__":
    # Sample input representing the ingestion layer schema
    sample_record = {
        "metadata": {
            "poem_id": "704",
            "poet": {"name": "لبيد بن ربيعة العامري", "gender": "Male", "era": "الجاهلي"},
            "poem_info": {"genre": "فخر"}
        },
        "poem_text": "سَعَى خُزَيْمَةُ فِي قَوْم لِيُهْلِكَهُمْ *** لَى الْحَمَّالَةِ هَلْ بِالْمَرْءِ مِنْ كَلْب"
    }
    
    process_poem_record(sample_record)
