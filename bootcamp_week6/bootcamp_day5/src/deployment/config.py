import os

MODEL_VERSION = os.getenv("MODEL_VERSION", "v1")

BASE_DIR = os.getcwd()

MODEL_DIR = os.path.join(BASE_DIR, "artifacts", "models")
LOG_PATH = os.path.join(BASE_DIR, "logs", "prediction_logs.csv")
