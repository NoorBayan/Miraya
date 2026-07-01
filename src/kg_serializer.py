from typing import Dict, Any
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from rdflib.namespace import XSD

def serialize_to_rdf(validated_json: Dict[str, Any]) -> str:
    """
    Transforms the verified JSON ontology payload into standard W3C RDF triples.
    Supports complex graph-based querying for the Digital Humanities infrastructure.
    """
    graph = Graph()
    ONTO = Namespace("http://maraya.ontology.org/schema#")
    DATA = Namespace("http://maraya.ontology.org/data/")
    
    graph.bind("maraya", ONTO)
    graph.bind("data", DATA)
    
    record_id = validated_json.get('record_id', 'unknown')
    event_uri = URIRef(DATA[f"Event_{record_id}"])
    
    graph.add((event_uri, RDF.type, ONTO.PoeticEvent))
    graph.add((event_uri, ONTO.hasTense, Literal(validated_json.get("main_event_tense", "unknown"))))
    graph.add((event_uri, ONTO.hasMood, Literal(validated_json.get("main_event_mood", "unknown"))))
    graph.add((event_uri, ONTO.hasAgencyType, Literal(validated_json.get("agency_type", "unknown"))))
    graph.add((event_uri, ONTO.hasGazeDirection, Literal(validated_json.get("gaze_direction", "none"))))
    
    woman_role = validated_json.get("woman_role", "none")
    if woman_role != "none":
        woman_node = URIRef(DATA[f"WomanParticipant_{record_id}"])
        graph.add((woman_node, RDF.type, ONTO.FemaleParticipant))
        graph.add((woman_node, ONTO.hasSemanticRole, Literal(woman_role)))
        graph.add((event_uri, ONTO.hasParticipant, woman_node))

    man_role = validated_json.get("man_role", "none")
    if man_role != "none":
        man_node = URIRef(DATA[f"ManParticipant_{record_id}"])
        graph.add((man_node, RDF.type, ONTO.MaleParticipant))
        graph.add((man_node, ONTO.hasSemanticRole, Literal(man_role)))
        graph.add((event_uri, ONTO.hasParticipant, man_node))
        
    graph.add((event_uri, ONTO.hasConfidenceProfile, Literal(validated_json.get("confidence", "Low"))))
    
    return graph.serialize(format="turtle")
