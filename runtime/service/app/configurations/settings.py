from pydantic import BaseSettings

class Settings(BaseSettings):
    checkpoint_dir: str = '/app/services/checkpoint/run1'
    MLFLOW_TRACKING_USERNAME: str = "user_name"
    MLFLOW_TRACKING_PASSWORD: str = "password"
    QNAMAKER_RUN_ID: str = 'run_id'
    artifact_uri: str = 'mlflow-artifacts:/406003722057627999/8708ee0cda534605b105c9e6bd333824/artifacts/checkpoint'

def get_settings():
    return Settings()
