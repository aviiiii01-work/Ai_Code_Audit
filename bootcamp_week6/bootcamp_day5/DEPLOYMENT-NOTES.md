# Loan Prediction API & Monitoring Deployment Notes

## 1. Overview
This project provides an end-to-end deployment of a Loan Approval Prediction API with monitoring capabilities. The system includes FastAPI backend for predictions, Joblib-based ML model loading, logging of all requests and predictions, Streamlit dashboard for monitoring data drift and prediction logs, and Docker-based deployment for easy environment consistency.

## 2. Project Structure
bootcamp_day5/
├── src/
│   ├── deployment/
│   │   ├── api.py
│   │   ├── model_loader.py
│   │   ├── schemas.py
│   │   ├── config.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── monitoring/
│       ├── dashboard.py
│       └── drift_checker.py
├── artifacts/
│   └── loan_model_v1.pkl
├── logs/
│   └── prediction_logs.csv
└── README.md

## 3. API Endpoints
GET / : Test endpoint to check API availability
POST /predict : Accepts loan applicant features and returns request_id, prediction (0 or 1), and probability (loan approval probability)

Sample Input JSON:
{"Gender": "Male", "Married": "Yes", "Dependents": "1", "Education": "Graduate", "Self_Employed": "No", "ApplicantIncome": 5000, "CoapplicantIncome": 0.0, "LoanAmount": 150.0, "Loan_Amount_Term": 360.0, "Credit_History": 1.0, "Property_Area": "Urban", "Total_Income": 5000.0, "Income_by_Loan": 33.33, "Loan_to_Income": 0.03, "EMI": 3500.0, "Balance_Income": 1500.0}

## 4. Running the API Locally
Using Python:
source venv/bin/activate
uvicorn src.deployment.api:app --reload --host 0.0.0.0 --port 8000

Using Docker:
docker build -t loan-api:day5 -f src/deployment/Dockerfile .
docker run -p 8000:8000 loan-api:day5

## 5. Monitoring Dashboard (Streamlit)
Set PYTHONPATH:
export PYTHONPATH=.
Run dashboard:
streamlit run src/monitoring/dashboard.py
Local URL: http://localhost:8501
Network URL: http://<your-ip>:8501
Dashboard Features: View prediction logs, check numeric data drift against training dataset, identify columns with drift beyond threshold

## 6. Logging
All prediction requests are logged in logs/prediction_logs.csv. Log columns include: request_id, timestamp, prediction, probability, and all input features.

## 7. Requirements
fastapi, uvicorn, pandas, scikit-learn, pydantic, joblib, streamlit, numpy

## 8. Notes & Best Practices
- Always ensure PYTHONPATH includes . when running Streamlit or Python modules directly.
- The API expects the trained model loan_model_v1.pkl in artifacts/.
- Use Docker for consistent deployment across machines.
- Keep logs/prediction_logs.csv persistent to monitor data drift over time.
- The Streamlit dashboard uses this log file to compute drift; ensure timestamp columns exist and are parsed correctly.
