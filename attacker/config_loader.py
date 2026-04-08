import yaml
from pathlib import Path

def load_targets(config_file: str = "lab/targets.yaml"):
    path = Path(config_file)

    with path.open("r", encoding ="utf-8") as file:
        data = yaml.safe_load(file)
    
    return data["targets"]