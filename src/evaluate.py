from joblib import load
import json
from pathlib import Path
import os
from sklearn.metrics import accuracy_score

from train import load_data


def main(repo_path):
    test_csv_path = repo_path / "data/prepared/test.csv"
    test_data, labels = load_data(test_csv_path)
    model = load(repo_path / "model/model.joblib")
    predictions = model.predict(test_data)
    accuracy = accuracy_score(labels, predictions)
    metrics = {"accuracy": accuracy}
    if not os.path.exists(repo_path / "metrics"):
        os.makedirs(repo_path / "metrics")
    accuracy_path = repo_path / "metrics/accuracy.json"
    with open(repo_path / "metrics/accuracy.json",'w') as file:
        json.dump(metrics,file)


if __name__ == "__main__":
    repo_path = Path(__file__).parent
    main(repo_path)