class MedicalDiagnosis:
    def __init__(self):
        self.symptoms = {
            'fever': 'Possible flu or infection.',
            'cough': 'Possible respiratory infection.',
            'headache': 'Possible stress, dehydration, or infection.',
            'fatigue': 'Possible anemia or sleep disorder.'
        }

    def diagnose(self, symptoms_list):
        diagnosis = []
        for symptom in symptoms_list:
            diagnosis.append(self.symptoms.get(symptom, "Symptom unknown"))
        return diagnosis

medical_system = MedicalDiagnosis()
patient_symptoms = ['fever', 'cough']
diagnosis = medical_system.diagnose(patient_symptoms)
print("Diagnosis:", diagnosis)
