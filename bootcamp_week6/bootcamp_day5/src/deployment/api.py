import os
from fastapi import FastAPI
import pandas as pd
from uuid import uuid4
from datetime import datetime, timezone

from src.deployment.schemas import LoanInput
from src.deployment.model_loader import load_model
from src.deployment.config import LOG_PATH

app = FastAPI(title="Loan Approval Prediction API")

model = load_model()


@app.get("/")
def greet():
    return ({"Greetings": "Namaste!, kya haal hai testing chal rahi hai"})

@app.post("/predict")
def predict(input_data: LoanInput):
    request_id = str(uuid4())
    input_df = pd.DataFrame([input_data.model_dump()])

    probability = model.predict_proba(input_df)[0][1]
    prediction = int(probability >= 0.5)    

    log_row = {
        "request_id": request_id,
        "timestamp": datetime.now(timezone.utc),
        "prediction": prediction,
        "probability": probability,
        **input_data.model_dump()
    }

    # Append to log
    pd.DataFrame([log_row]).to_csv(
        LOG_PATH,
        mode="a",
        header=not os.path.exists(LOG_PATH),
        index=False
    )

    return {
        "request_id": request_id,
        "prediction": prediction,
        "probability": round(probability, 4)
    }
