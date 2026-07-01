import json
import logging
from typing import Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def _execute_bounded_generation(prompt_string: str) -> str:
    """
    Interfaces with the foundational model using a deterministic configuration 
    (Temperature = 0.1, Top-p = 1.0) to minimize stochastic hallucination.
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0.1, 
        top_p=1.0,
        max_output_tokens=4096
    )
    response = llm.invoke(prompt_string)
    return response.content

def run_ontology_inference(payload: Dict[str, Any], prompt_template: PromptTemplate) -> Dict[str, Any]:
    """
    Executes the Neuro-Symbolic inference layer, transforming textual ambiguity 
    into a candidate semantic JSON payload.
    """
    formatted_prompt = prompt_template.format(
        verse_text=payload["normalized_text"],
        poet_name=payload["context_metadata"]["poet_name"],
        poet_gender=payload["context_metadata"]["poet_gender"],
        era=payload["context_metadata"]["era"],
        genre=payload["context_metadata"]["genre"]
    )
    
    raw_output = _execute_bounded_generation(formatted_prompt)
    
    try:
        clean_json_string = raw_output.replace("```json", "").replace("```", "").strip()
        candidate_json = json.loads(clean_json_string)
        candidate_json["record_id"] = payload["record_id"]
        return candidate_json
    except json.JSONDecodeError as e:
        logging.error(f"Inference schema violation for Record {payload['record_id']}: {str(e)}")
        return {
            "record_id": payload["record_id"],
            "status": "Schema_Violation",
            "confidence": "Low",
            "review_flags": ["JSON Parsing Failure"]
        }
