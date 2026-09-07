import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. نص تقرير طبي غير مهيكل (نموذج محاكاة لتقرير مستشفى)
clinical_note = """
PATIENT MEDICAL REPORT
Patient: Male, 45 years old.
Chief Complaint: Patient presents with severe chest pain, shortness of breath, and mild fatigue.
Diagnosis: Confirmed Acute Myocardial Infarction with Hypertension.
Prescription Plan:
- Aspirin 100mg daily
- Metoprolol 50mg twice daily
- Atorvastatin 40mg at bedtime
Follow-up: Re-evaluate in 2 weeks.
"""

# 2. دوال الاستخراج باستخدام التعبيرات النمطية (Regular Expressions)
def parse_clinical_report(text):
    # استخراج العمر والجنس
    age_match = re.search(r'(\d+)\s*years\s*old', text, re.IGNORECASE)
    gender_match = re.search(r'Patient:\s*(Male|Female)', text, re.IGNORECASE)
    
    # استخراج التشخيص
    diagnosis_match = re.search(r'Diagnosis:\s*(.*?)(?=\n|Prescription)', text, re.DOTALL)
    
    # استخراج الأعراض
    symptoms_match = re.search(r'Chief Complaint:\s*(.*?)(?=\n|Diagnosis)', text, re.DOTALL)
    
    # استخراج الأدوية والجرعات
    medications = re.findall(r'-\s*([A-Za-z]+)\s*(\d+mg.*?)(?=\n|$)', text)

    return {
        "Age": age_match.group(1) if age_match else "N/A",
        "Gender": gender_match.group(1) if gender_match else "N/A",
        "Diagnosis": diagnosis_match.group(1).strip() if diagnosis_match else "N/A",
        "Symptoms": [s.strip() for s in symptoms_match.group(1).replace("Patient presents with", "").split(",")] if symptoms_match else [],
        "Medications": [{"Drug": med[0], "Dosage": med[1].strip()} for med in medications]
    }

# 3. معالجة النص وتحويله إلى جدول بيانات
parsed_data = parse_clinical_report(clinical_note)

print("==================================================")
print("       EXTRACTED STRUCTURED MEDICAL DATA          ")
print("==================================================")
print(f"Patient Demographic : {parsed_data['Age']} y/o {parsed_data['Gender']}")
print(f"Primary Diagnosis   : {parsed_data['Diagnosis']}")
print(f"Extracted Symptoms  : {', '.join(parsed_data['Symptoms'])}")
print("==================================================")

# تحويل الأدوية إلى DataFrame لتصديرها ومعاينتها
df_meds = pd.DataFrame(parsed_data['Medications'])
print("\nExtracted Prescriptions:")
print(df_meds.to_string(index=False))

# حفظ البيانات المهيكلة في ملف CSV
df_meds.to_csv("extracted_prescriptions.csv", index=False)

# 4. رسم بياني توضيحي للعرض على LinkedIn (Symptom & Medication Distribution)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 4))

drugs = [m['Drug'] for m in parsed_data['Medications']]
dosages = [m['Dosage'] for m in parsed_data['Medications']]

bars = ax.barh(drugs, [100, 50, 40], color=['#1f77b4', '#ff7f0e', '#2ca02c'])
ax.set_title("Clinical NLP: Extracted Medications & Dosage Overview", fontsize=12, pad=15)
ax.set_xlabel("Dosage Value Reference (mg)")
ax.bar_label(bars, labels=dosages, padding=5)

plt.tight_layout()
plt.savefig("clinical_analysis_chart.png", dpi=300)
plt.show()