from pathlib import Path
import joblib

MODEL_PATH = Path("artifacts/models/loan_model_v1.pkl")  

def load_model():
    model = joblib.load(MODEL_PATH)
    return model
