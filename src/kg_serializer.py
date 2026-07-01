from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.namespace import XSD

def serialize_to_rdf(accepted_json: dict) -> str:
    """
    Transforms validated semantic records into an auditable Knowledge Graph (RDF format).
    Preserves provenance and epistemic status as formal graph properties (Section 5.5).
    """
    g = Graph()
    ONTO = Namespace("http://maraya.ontology.org/schema#")
    DATA = Namespace("http://maraya.ontology.org/data/")
    
    g.bind("maraya", ONTO)
    
    record_id = accepted_json.get('record_id', 'unknown')
    event_node = URIRef(DATA[f"Event_{record_id}"])
    
    # Core Ontology Hierarchies
    g.add((event_node, RDF.type, ONTO.PoeticEvent))
    g.add((event_node, ONTO.hasMainDescription, Literal(accepted_json.get("main_event", ""))))
    g.add((event_node, ONTO.hasAgencyType, Literal(accepted_json.get("agency_type", "N/A"))))
    g.add((event_node, ONTO.hasGazeDirection, Literal(accepted_json.get("gaze_direction", "N/A"))))
    
    # Process Relational Role Dynamics (Gender & Agency)
    for role_obj in accepted_json.get("man_roles_all", []):
        participant_node = URIRef(DATA[f"Participant_{hash(role_obj['entity'])}"])
        g.add((participant_node, RDF.type, ONTO.MaleParticipant))
        g.add((event_node, ONTO.hasParticipant, participant_node))
        g.add((participant_node, ONTO.hasRole, Literal(role_obj['role'])))

    # Preserve Uncertainty as Epistemic Provenance
    g.add((event_node, ONTO.hasConfidenceScore, Literal(accepted_json.get("confidence_score", 0.0), datatype=XSD.float)))
    
    return g.serialize(format="turtle")
