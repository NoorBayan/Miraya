from langchain.prompts import PromptTemplate

def build_ontology_prompt() -> PromptTemplate:
    """
    Constructs the ontology-guided prompt template (Section 5.2).
    Enforces strict vocabulary boundaries and JSON schema compliance.
    """
    template = """
    You are an expert in Classical Arabic Literature and Ontology Engineering.
    Analyze the following verse based on its historical and morphological context.
    
    Verse: {verse_text}
    Poet: {poet_name} (Gender: {poet_gender})
    Era: {era}
    Genre: {genre}
    
    You MUST output a valid JSON matching this exact schema and ONLY use allowed ontology classes.
    
    Schema Constraints:
    - main_event: string (brief summary)
    - events: array of strings (explicit and implicit verb lemmas)
    - participants: array of strings (entities involved)
    - speaker_gender: ["Male", "Female", "Unknown"]
    - man_roles_all: array of objects {{"entity": string, "role": ["Agent", "Patient", "Theme", "Experiencer", "Addressee"]}}
    - woman_roles_all: array of objects {{"entity": string, "role": ["Agent", "Patient", "Theme", "Experiencer", "Addressee"]}}
    - agency_type: ["Speech Act", "Emotional", "Social/Political", "Domestic", "Intellectual", "N/A"]
    - objectification_type: ["Fragmented", "Holistic", "Ornamental", "Sensual", "N/A"]
    - gaze_direction: ["Male-to-Female", "Female-to-Male", "Mutual", "Self-Gaze", "N/A"]
    - confidence_score: float (0.0 to 1.0)
    - review_flags: array of strings (e.g., ["Ambiguity", "Heavy Metaphor"])
    
    Output JSON ONLY. No markdown wrappers, no explanations.
    """
    
    prompt = PromptTemplate(
        input_variables=["verse_text", "poet_name", "poet_gender", "era", "genre"],
        template=template
    )
    return prompt
