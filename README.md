# 🩺 Clinical Notes NLP Parser

A Python-based Natural Language Processing (NLP) tool designed for HealthTech and Clinical Data Processing. This script automatically parses unstructured clinical notes and extracts key medical information (demographics, diagnoses, symptoms, and prescriptions) into structured formats.

---

## 🚀 Key Features

- Demographics Extraction: Automatically identifies patient age and gender.
- Clinical Findings: Extracts chief complaints, symptoms, and confirmed medical diagnoses using Regular Expressions (re).
- Prescription Structuring: Parses medications, dosages, and schedules into a structured Pandas DataFrame and exports to .csv.
- Clinical Data Visualization: Generates dark-themed dosage summary charts using Matplotlib and Seaborn.

---

## 🛠️ Tech Stack

- Language: Python 3.11+
- Data Manipulation: pandas
- Text Processing & Regex: re
- Data Visualization: matplotlib, seaborn

---

## 📊 Sample Input & Extracted Output

### Input (Unstructured Note)
> *"Patient: Male, 45 years old. Chief Complaint: Severe chest pain, shortness of breath... Diagnosis: Confirmed Acute Myocardial Infarction..."*

### Extracted Structured Data
| Patient Demographic | Primary Diagnosis | Extracted Prescriptions |
| :--- | :--- | :--- |
| 45 y/o Male | Acute Myocardial Infarction | Aspirin (100mg), Metoprolol (50mg), Atorvastatin (40mg) |

---

## 🏃 How to Run

1. Clone this repository:
   https://github.com/s-sy36/clinical-notes-nlp-parser.git
   
Install dependencies:
pip install pandas matplotlib seaborn

Execute the parser script:
python clinical_parser.py





   
