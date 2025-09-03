# Miraya  
*A Critically Validated Computational Corpus for Arabic Poetry and Feminist Analysis*

---

## 🌟 Overview  
**Miraya** is the largest **critically validated computational corpus** of Arabic poetry to date.  
It combines large-scale datafication with feminist critical methodologies to examine how gender, power, and cultural memory are encoded in Arabic poetic traditions.  

The corpus spans more than **14 million verses** across 16 major categories, annotated with rich metadata (genre, prosody, meter, historical period, geography, and poet demographics).  
Its distinctive contribution lies in treating **archival biases not as limitations but as data**—foregrounding how Arabic poetic heritage functions as a *technology of gender*.  

---

## 📂 Repository Structure  


---



---

## ⚙️ Methodology  
Miraya employs a **hybrid validated approach**:  

1. **Ground Truth Construction**  
   - A stratified random sample of 500–1000 verses was hand-annotated by experts.  
   - Annotation schema covered *objectification* and *agency*.  
   - Inter-Annotator Agreement (IAA) was measured (Krippendorff’s Alpha).  

2. **LLM Pipeline Development & Validation**  
   - Iterative prompt engineering was used to optimize performance.  
   - Model outputs were compared against the gold standard dataset.  
   - Performance metrics (Precision, Recall, F1-score) ensured reliability (F1 > 0.85 threshold).  

3. **Full-Scale Application**  
   - The validated pipeline was applied to the entire corpus.  
   - Human-in-the-loop auditing was performed on anomalies and outliers.  

4. **Radical Transparency**  
   - All prompts, annotation guidelines, and validation datasets are made publicly available in this repository.  

---

## 🔍 Features  
- **Largest scale**: 14M verses spanning from pre-Islamic to contemporary poetry.  
- **Rich annotations**: Genres, meters, rhymes, periods, geographies, poet demographics.  
- **Feminist-critical framing**: Biases (e.g., 96% male dominance, archival silences) treated as data.  
- **Validated pipeline**: Empirical LLM validation ensures reliable automated analysis.  
- **Open science**: Full reproducibility via deposited code, guidelines, and benchmark datasets.  

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.10+  
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `transformers`, `matplotlib`, `ipywidgets`  

### Quick Start  

Clone the repository:  
```bash
git clone https://github.com/username/Miraya.git
cd Miraya
