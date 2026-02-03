import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

MODEL_PATH = "models/tuned_random_forest.pkl"
DATA_PATH = "data/processed/features.csv"
OUTPUT_DIR = "evaluation/shap_outputs"


def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Loan_Status"] = df["Loan_Status"].map({"N": 0, "Y": 1})
    X = df.drop("Loan_Status", axis=1)
    return X


def get_positive_class_shap(shap_values):
    if isinstance(shap_values, list):
        return shap_values[1]
    if isinstance(shap_values, np.ndarray) and shap_values.ndim == 3:
        return shap_values[:, :, 1]
    return shap_values


def main():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    pipeline = joblib.load(MODEL_PATH)
    X = load_data()

    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["classifier"]

    X_transformed = preprocessor.transform(X)
    feature_names = preprocessor.get_feature_names_out()

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_transformed)

    shap_values_pos = get_positive_class_shap(shap_values)

    shap.summary_plot(
        shap_values_pos,
        X_transformed,
        feature_names=feature_names,
        show=False
    )
    plt.savefig(f"{OUTPUT_DIR}/shap_summary.png", dpi=300, bbox_inches="tight")
    plt.close()

    shap.summary_plot(
        shap_values_pos,
        X_transformed,
        feature_names=feature_names,
        plot_type="bar",
        show=False
    )
    plt.savefig(f"{OUTPUT_DIR}/shap_feature_importance.png", dpi=300, bbox_inches="tight")
    plt.close()

    shap.dependence_plot(
        feature_names[0],
        shap_values_pos,
        X_transformed,
        feature_names=feature_names,
        show=False
    )
    plt.savefig(f"{OUTPUT_DIR}/shap_dependence_example.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("SHAP analysis completed successfully")
    print(f"Artifacts saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
