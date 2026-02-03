import os
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler


RAW_DATA_PATH = "data/raw/loan_data.csv"
PROCESSED_DATA_PATH = "data/processed/final.csv"


def load_data(path):
    return pd.read_csv(path)    


def remove_duplicates(df):
    return df.drop_duplicates()


def handle_missing_values(df):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(df[col].median())
    return df


def handle_outliers(df, numeric_cols):
    for col in numeric_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75) 
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    return df


def encode_target(df):
    df["Loan_Status"] = df["Loan_Status"].map({"Y": 1, "N": 0})
    return df


def scale_features(df, numeric_cols):
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df


def save_data(df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def run_pipeline():
    df = load_data(RAW_DATA_PATH)
    df = df.drop(columns=['Loan_ID'])
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    df = encode_target(df)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    numeric_cols.remove("Loan_Status")

    df = handle_outliers(df, numeric_cols)
    df = scale_features(df, numeric_cols)

    save_data(df, PROCESSED_DATA_PATH)



if __name__ == "__main__":
    run_pipeline()
