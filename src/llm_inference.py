import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

def run_llm_inference(payload: dict, prompt_template: PromptTemplate) -> dict:
    """
    Executes the neuro-symbolic interface layer using low-temperature LLM generation
    to ensure bounded contextual parsing (Section 5.2).
    """
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)
    
    formatted_prompt = prompt_template.format(
        verse_text=payload["normalized_text"],
        poet_name=payload["context_metadata"]["poet_name"],
        poet_gender=payload["context_metadata"]["poet_gender"],
        era=payload["context_metadata"]["era"],
        genre=payload["context_metadata"]["genre"]
    )
    
    try:
        response = llm.invoke(formatted_prompt)
        candidate_json = json.loads(response.content)
        candidate_json["record_id"] = payload["record_id"]
        return candidate_json
    except json.JSONDecodeError:
        return {
            "record_id": payload["record_id"],
            "status": "Error",
            "message": "Model generated invalid JSON structure.",
            "confidence_score": 0.0
        }
