import mlflow
import os
from pathlib import Path

mlflow.tracking.set_tracking_uri("http://localhost:5000/")

def load_model_mlflow():
    mlflow.set_experiment('log artifacts')
    artifact_uri = "mlflow-artifacts:/406003722057627999/8708ee0cda534605b105c9e6bd333824/artifacts/checkpoint"
    RESOURCE_PATH = os.getcwd() + '\\app\\services\\checkpoint'
    file_path = Path(os.path.join(RESOURCE_PATH))
    print(file_path)
    
    if ~file_path.exists():
        mlflow.artifacts.download_artifacts(artifact_uri, dst_path=file_path)