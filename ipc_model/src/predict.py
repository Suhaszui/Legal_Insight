import joblib
from rules import apply_rules
from sklearn.pipeline import Pipeline
pipeline=joblib.load(r'C:\legal_ai_project\ipc_model\models\ipc_pipeline.joblib')

def predict_ipc(text: str) -> str:
    ml_pred = pipeline.predict([text])[0]
    final_pred = apply_rules(text, ml_pred)
    return final_pred
