# 🪞 Miraya: Semantic and Gender Ontology of Classical Arabic Poetry

Welcome to **Miraya**, the most comprehensive structured semantic dataset and knowledge graph for the study of Classical Arabic Poetry. Moving beyond traditional surface-level Natural Language Processing (NLP) tasks such as sentiment analysis or meter classification, **Miraya** provides a deep semantic representation that deconstructs narrative structures, semantic roles, and gender representations within poetic texts.

Designed as an open research resource, **Miraya** is specifically engineered to support advanced studies in **Digital Humanities**, **Computational Literary Studies**, and **Feminist Literary Criticism**, translating highly abstract literary concepts—such as the male gaze, physical objectification, and agency deprivation—into measurable, computable, and query-ready variables.

---

## 🌟 Why This Dataset? (Research & Critical Value)

This ontology opens unprecedented avenues for cultural studies and critical theory by enabling quantitative-qualitative analysis of the following phenomena:

* 👁️ **Gaze Dynamics:** Tracks the directionality of the physical and descriptive gaze (e.g., Male-to-Female, Female-to-Male, Mutual, Self-Gaze). This allows researchers to empirically test theories of the "Male Gaze" and document who possesses descriptive authority in the text.
* 🧩 **Objectification:** Provides a precise taxonomy of physical description (Fragmented, Holistic, Ornamental, Sensual). This enables the study of how characters (particularly women) are reduced to body parts or aesthetic ornaments.
* ⚙️ **Agency & Semantic Roles:** We do not merely count the appearance of male or female entities; we assign explicit **Semantic Roles** (Agent, Patient, Theme, Experiencer). Is the female figure an active initiator of events or a passive recipient?
* 🎭 **Agency Typology:** Categorizes the domain of actions (Social/Political, Emotional, Domestic, Speech Act), revealing the gendered limitations of permissible actions within the poetic imagination.

---

## 📂 JSON Schema Structure

The dataset is structured as a nested JSON to accurately represent the complex relationships between entities, events, and descriptors. Each poem acts as a central **Node** comprising six primary categories:

### 1. `metadata`
The historical and authorial context of the text.
* `poet`: Demographics (Name, Gender, Era, Nationality, Biography ID).
* `poem_info`: Title, Form, Genre, and Core Theme (`theme_id`).
* `prosody`: Linguistic and metrical features (Meter, Submeter, Rhyme).

### 2. `content`
* `poem_text`: The complete string of the verse.
* `verses`: A perfectly parsed array of hemistichs.

### 3. `semantic_analysis`
Deconstructs the core narrative event.
* `events_list`: An array of verbs, distinguishing between explicit verbs and contextually inferred/implicit actions (`is_implicit`).
* `main_event`: Contains the central event description, verb lemma, tense, polarity, and grammatical mood.

### 4. `participants_and_roles`
Answers the fundamental question: *Who does what to whom?*
* `speaker`: Is the poet actively present in the event? What is their inferred gender?
* `gender_inference_basis`: How was gender deduced? (Explicit Word, Morphology, Literary Context).
* `all_roles`: Two arrays (`women` and `men`) listing every human entity alongside their specific semantic role.

### 5. `advanced_gender_metrics`
The core of the gender analysis.
* `descriptors`: Detailed lists and counts of physical descriptions, with a `linked_list` mapping each descriptor precisely to its target entity.
* `agency_events`: A strict inventory of actions where male or female entities operate as the *Agent*.
* `nonhuman_entities`: Anthropomorphized or rhetorically active non-human entities (e.g., Time, Sword, Fate).

### 6. `literary_analytics_and_review`
The abstract critical layer.
* `objectification_type`: The nature of bodily representation (Fragmented, Sensual, etc.).
* `agency_type`: The domain of the main event's agency.
* `gaze_direction`: The vector of the descriptive gaze.
* `thematic_tags`: Core motifs (Love, War, Pride).
* `quality_control`: The extraction confidence score and `review_flags` highlighting instances of genuine literary ambiguity or heavy metaphor.

---

## 🔍 Critical Data Dictionary

To facilitate cultural and literary analysis, key fields are operationalized as follows:

| Field | Critical Application |
| :--- | :--- |
| **`objectification_type`** | Measures how the body is perceived. Is it deconstructed into parts (`Fragmented` e.g., waist, eyes), viewed entirely (`Holistic`), used for arousal (`Sensual`), or treated as jewelry (`Ornamental`)? |
| **`agency_type`** | Reveals whether female agency is confined to `Emotional` or `Domestic` spheres, while male agency dominates `Social/Political` domains. |
| **`is_implicit`** | Implicit actions enclosed in brackets `[ ]` are crucial for uncovering "hidden agency" or suppressed power dynamics that are not grammatically explicit in the text. |
| **`review_flags`** | Contains tags like `Heavy Metaphor` or `Gender Unclear`. In computational humanities, ambiguity is not treated as an error but as deliberate rhetorical data to be studied. |

---

## 💡 Suggested Research Questions

Designed for scholars of Middle Eastern literature and gender studies, this dataset provides empirical grounding for profound critical inquiries:

1. **The Diachronic Evolution of Objectification:** How did the "Fragmented" objectification of the female body transition from the Pre-Islamic (Jahili) era through the Abbasid period? 
2. **Agency Deprivation and Genre Norms:** By cross-referencing `woman_roles_all` with `poem_genre`, can we trace the systematic shift of the female figure from an active *Agent* in elegiac poetry (Ritha') to a passive *Theme/Patient* in amatory poetry (Ghazal)?
3. **Subversion of the Gaze:** Are there specific historical epochs or poetic sub-genres where the *Mutual Gaze* or *Female-to-Male* gaze significantly disrupts traditional patriarchal descriptive norms?
4. **Metaphorical Displacement of Power:** Is there a quantifiable correlation between the rise of active non-human entities (`nonhuman_entities` like *Fate* or *Time*) and the suppression of explicit female agency (`agency_type`) in classical verse?

---

## 🚀 Exploratory Tools & Services

To facilitate immediate engagement with the dataset, we have provided an accompanying Jupyter Notebook featuring four ready-to-use analytical services that bridge computational logic with literary criticism:

1. **Semantic Poem Explorer:**  
   Filter by era, genre, or poet gender. The system retrieves matching verses with interactive HTML highlighting, instantly visualizing the main event, the agent, the patient, and the objectification type directly on the Arabic text.
2. **Agency & Objectification Dashboard:**  
   A powerful Distant Reading tool. Select a specific literary context to generate visual progress bars comparing male vs. female agency (Active vs. Passive) and the dominant modes of objectification within that era.
3. **Interaction & Gaze Network Viewer:**  
   Translates the poetic verse into a Knowledge Graph matrix (Subject → Gaze/Action → Object). This exposes the underlying relational network, clarifying exactly who directs the gaze and who receives it.
4. **Diachronic Trend Tracker:**  
   Select a critical phenomenon (e.g., *Sensual Objectification*) to instantly generate temporal visualizations showing how this literary device evolved, peaked, or declined across the 12 classical Arabic eras.

---

## 📜 License & Citation
[Insert your specific license here, e.g., CC BY-NC 4.0]

If you utilize this dataset or its schema in your academic research, please cite the following paper:  
`[Citation details will be added upon publication in IEEE Access]`
