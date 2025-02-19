# 🧬 ncRNA Prioritization Pipeline for Autoimmune & Inflammatory Pathways

This project provides an **in silico framework** to identify and prioritize non-coding RNAs (ncRNAs) involved in autoimmune and inflammatory pathways. It integrates various data sources and computational analyses into a modular pipeline.

---

## 🚀 **Pipeline Overview**
The pipeline is divided into seven modules:

1. **Predict ncRNA-Protein Interactions**  
2. **Curate and Integrate Autoimmune Pathway Data**  
3. **ncRNA Annotation and Characterization**  
4. **Feature Engineering** *(expression data, GWAS loci, RNA structure, RNA-binding motifs)*  
5. **Prioritize ncRNAs Based on Functional Relevance**  
6. **Network Visualization and Interaction Analysis**  
7. **Report Generation** *(data visualizations & summary)*  

---

## 🗂️ **Project Structure**
```
ncRNA_pipeline/
├── data/                # Input data files (expression data, pathways, etc.)
├── outputs/             # Output results and visualizations
├── scripts/             # Python modules for each pipeline step
│   ├── 1_interaction_prediction.py
│   ├── 2_pathway_curation.py
│   ├── 3_annotation.py
│   ├── 4_feature_engineering.py
│   ├── 5_prioritization.py
│   ├── 6_network_analysis.py
│   └── 7_report_generation.py
├── requirements.txt    # Python dependencies
├── README.md           # Project overview and usage instructions
└── .gitignore          # Ignored files and folders
```

---

## 💻 **Installation**
1. **Clone the repository:**  
```bash
git clone https://github.com/imrobintomar/ncRNA_pipeline.git
cd ncRNA_pipeline
```

2. **Create and activate a virtual environment:**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**  
```bash
pip install -r requirements.txt
```

---

## ⚙️ **Usage**
Each script can be run independently or as part of a complete pipeline. 

### Run Individual Steps:
```bash
python scripts/1_interaction_prediction.py --input data/ncrnas.csv --output outputs/interactions.csv
python scripts/2_pathway_curation.py --output outputs/pathways.csv
```

### Run Full Pipeline:
```bash
bash run_pipeline.sh  # (If you create a shell script to automate all steps)
```

---

## 📊 **Example Output**
- Prioritized ncRNA list with functional scores  
- Network visualizations of ncRNA-RBP-pathway interactions  
- Comprehensive PDF/HTML reports with plots and tables  

---

## 🧩 **Contributing**
Pull requests and issues are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## 📄 **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 **Acknowledgments**
This pipeline leverages resources from:
- [RNAcentral](https://rnacentral.org/)
- [Gene Ontology (GO)](http://geneontology.org/)
- [GWAS Catalog](https://www.ebi.ac.uk/gwas/)
- [STRING Database](https://string-db.org/)
- Open-source Python libraries (Pandas, Scikit-learn, NetworkX, etc.)

---

## 📫 **Contact**
For questions or collaboration opportunities, reach out at [itsrobintomar@gmail.com](mailto:itsrobintomar@gmail.com).  

---

⭐️ If you find this project useful, give it a star on GitHub!
