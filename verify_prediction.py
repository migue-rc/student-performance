import pandas as pd
import joblib
import os

model_path = 'model_pipeline.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
    
    # Default sample student (with the fix)
    sample = {
        'Hours_Studied': [20], 'Attendance': [90], 'Sleep_Hours': [7], 'Previous_Scores': [80],
        'Tutoring_Sessions': [2], 'Physical_Activity': [3], 'Parental_Involvement': ['Medium'],
        'Access_to_Resources': ['Medium'], 'Extracurricular_Activities': ['Yes'],
        'Motivation_Level': ['Medium'], 'Internet_Access': ['Yes'], 'School_Type': ['Public'],
        'Peer_Influence': ['Neutral'], 'Learning_Disabilities': ['No'],
        'Parental_Education_Level': ['High School'], 'Distance_from_Home': ['Near'],
        'Gender': ['Male'], 'Teacher_Quality': ['Medium'], 'Family_Income': ['Medium']
    }
    
    df_s = pd.DataFrame(sample)
    df_s["Study_Intensity"] = df_s["Hours_Studied"] * (df_s["Attendance"] / 100)
    df_s["Academic_Effort"] = df_s["Hours_Studied"] + df_s["Tutoring_Sessions"]
    df_s["Study_Sleep_Balance"] = (df_s["Hours_Studied"] - (df_s["Sleep_Hours"] * 7))
    
    pred = model.predict(df_s)[0]
    print(f"Prediction successful: {pred:.2f}")
else:
    print("Model not found. Please render the modeling file first.")
