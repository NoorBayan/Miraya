from langchain.prompts import PromptTemplate

def build_ontology_prompt() -> PromptTemplate:
    """
    Constructs the ontology-guided prompt template. 
    Strictly enforces the semantic schema, vocabularies, and categorical boundaries 
    defined in the system architecture.
    """
    template = """
    You are an expert Semantic Knowledge Engineer specializing in Classical Arabic Literature.
    Perform a deep semantic extraction on the following verse, strictly adhering to the provided ontology.
    
    Verse: {verse_text}
    Context: Poet: {poet_name} | Gender: {poet_gender} | Era: {era} | Genre: {genre}
    
    OUTPUT FORMAT: You MUST output ONLY a valid JSON object matching this exact schema. Do not generate markdown.
    
    SCHEMA & ALLOWED VALUES:
    - main_event: string (A concise summary of the primary action)
    - main_event_tense: ["Past", "Present", "Future", "Imperative", "Timeless", "unknown"]
    - main_event_polarity: ["Affirmative", "Negated", "Ambiguous (conditional)", "Ambiguous (interrogative)", "unknown"]
    - main_event_mood: ["Indicative", "Imperative", "Conditional", "Subjunctive", "Jussive", "Optative", "Interrogative", "unknown"]
    - speaker_present: ["Yes", "No", "unknown"]
    - speaker_gender: ["Male", "Female", "unknown"]
    - gender_inference_basis: ["Explicit Word", "Morphology", "Proper Name", "Literary Context", "Assumed", "none"]
    - woman_role: ["Agent", "Patient", "Theme", "Experiencer", "Addressee", "none", "Other"]
    - man_role: ["Agent", "Patient", "Theme", "Experiencer", "Addressee", "none", "Other"]
    - objectification_type: ["Holistic", "Fragmented", "Ornamental", "Sensual", "Mutual", "none"]
    - agency_type: ["Speech Act", "Emotional", "Social/Political", "Domestic", "Intellectual", "War", "Travel", "Mutual", "unknown"]
    - gaze_direction: ["Male-to-Female", "Female-to-Male", "Mutual", "Self-Gaze", "Male-to-Character", "Narrator-to-Character", "none"]
    - confidence: ["High", "Medium", "Low"]
    - review_flags: array of strings (e.g., ["Heavy Metaphor", "Ambiguity", "Coreference Unclear"])
    """
    
    return PromptTemplate(
        input_variables=["verse_text", "poet_name", "poet_gender", "era", "genre"],
        template=template
    )
