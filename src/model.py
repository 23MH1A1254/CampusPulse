from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "placement_readiness.csv"
FEATURES = [
    "coding_score", "aptitude_score", "communication_score", "cgpa",
    "projects", "internships", "certifications", "hackathons"
]
TARGET = "placement_ready"

def train_model(data_path=DATA_PATH, random_state=42):
    data = pd.read_csv(data_path)
    X = data[FEATURES]
    y = data[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state, stratify=y
    )
    model = RandomForestClassifier(
        n_estimators=250, max_depth=8, min_samples_leaf=3,
        class_weight="balanced", random_state=random_state
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    metrics = {
        "accuracy": float(accuracy_score(y_test, pred)),
        "precision": float(precision_score(y_test, pred, zero_division=0)),
        "recall": float(recall_score(y_test, pred, zero_division=0)),
        "f1_score": float(f1_score(y_test, pred, zero_division=0))
    }
    return model, metrics

def get_trained_model():
    return train_model()
