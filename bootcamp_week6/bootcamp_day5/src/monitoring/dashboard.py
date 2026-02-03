import streamlit as st
import pandas as pd
from src.monitoring.drift_checker import check_data_drift

st.title("Loan Prediction Monitoring Dashboard")

log_path = "logs/prediction_logs.csv"
train_data_path = "data/processed/X_train.csv"

try:
    logs = pd.read_csv(log_path, parse_dates=['timestamp'])
    st.subheader("Recent Predictions")
    st.dataframe(logs.tail(10))
except FileNotFoundError:
    st.warning("No prediction logs found yet.")

if st.button("Check Data Drift"):
    report = check_data_drift(train_data_path, log_path)
    st.subheader("Data Drift Report")
    drift_df = pd.DataFrame(report).T
    st.dataframe(drift_df)
