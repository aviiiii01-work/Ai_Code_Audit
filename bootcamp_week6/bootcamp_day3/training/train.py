import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

try:
    from xgboost import XGBClassifier
    xgb_available = True
except:
    xgb_available = False


DATA_PATH = "data/processed/features.csv"
MODEL_OUTPUT_PATH = "models/best_model.pkl"
METRICS_PATH = "evaluation/metrics.json"
CONF_MATRIX_PATH = "evaluation/confusion_matrix.png"


def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Loan_Status"] = df["Loan_Status"].map({"N": 0, "Y": 1})
    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]
    return X, y


def build_preprocessor(X):
    categorical_cols = X.select_dtypes(include=["object"]).columns
    numerical_cols = X.select_dtypes(exclude=["object"]).columns

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                categorical_cols
            ),
            ("num", "passthrough", numerical_cols)
        ]
    )
    return preprocessor


def get_models(preprocessor):
    models = {
        "LogisticRegression": Pipeline([
            ("preprocess", preprocessor),
            ("model", LogisticRegression(
                max_iter=1000,
                solver="liblinear"
            ))
        ]),
        "RandomForest": Pipeline([
            ("preprocess", preprocessor),
            ("model", RandomForestClassifier(
                n_estimators=200,
                max_depth=10,
                random_state=42
            ))
        ]),
        "NeuralNetwork": Pipeline([
            ("preprocess", preprocessor),
            ("model", MLPClassifier(
                hidden_layer_sizes=(64, 32),
                max_iter=500,
                random_state=42
            ))
        ])
    }

    if xgb_available:
        models["XGBoost"] = Pipeline([
            ("preprocess", preprocessor),
            ("model", XGBClassifier(
                n_estimators=200,
                max_depth=5,
                learning_rate=0.1,
                eval_metric="logloss",
                random_state=42
            ))
        ])

    return models


def evaluate_models(X, y, models):
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    scoring = {
        "accuracy": "accuracy",
        "precision": "precision",
        "recall": "recall",
        "f1": "f1",
        "roc_auc": "roc_auc"
    }

    results = {}
    best_model_name = None
    best_score = -1

    for name, model in models.items():
        scores = cross_validate(
            model,
            X,
            y,
            cv=cv,
            scoring=scoring,
            error_score="raise"
        )

        avg_scores = {
            metric: float(np.mean(scores[f"test_{metric}"]))
            for metric in scoring
        }

        results[name] = avg_scores

        if avg_scores["roc_auc"] > best_score:
            best_score = avg_scores["roc_auc"]
            best_model_name = name 

    return results, best_model_name


def train_best_model(X, y, models, best_model_name):
    model = models[best_model_name]
    model.fit(X, y)
    joblib.dump(model, MODEL_OUTPUT_PATH)
    return model


def plot_confusion_matrix(model, X, y):
    preds = model.predict(X)
    cm = confusion_matrix(y, preds)

    plt.figure(figsize=(5, 4))
    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j], ha="center", va="center")

    plt.tight_layout()
    plt.savefig(CONF_MATRIX_PATH)
    plt.close()


def save_metrics(metrics, best_model_name):
    output = {
        "best_model": best_model_name,
        "metrics": metrics
    }
    with open(METRICS_PATH, "w") as f:
        json.dump(output, f, indent=4)


def run_training_pipeline():
    X, y = load_data()
    preprocessor = build_preprocessor(X)
    models = get_models(preprocessor)

    metrics, best_model_name = evaluate_models(X, y, models)
    best_model = train_best_model(X, y, models, best_model_name)

    plot_confusion_matrix(best_model, X, y)
    save_metrics(metrics, best_model_name)

    print("Day-3 Training Complete")
    print(f"Best Model: {best_model_name}")


if __name__ == "__main__":
    run_training_pipeline()
