from text_summarizer.utils.common import read_yaml, create_directories
from pathlib import Path
from typing import Dict

CONFIG_PATH = Path("config/config.yaml")
PARAMS_PATH = Path("parameters.yaml")

class ConfigManager:
    def __init__(self, config_filepath = CONFIG_PATH, params_filepath = PARAMS_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create artifacts directory
        create_directories([self.config["artifacts_root"]])

    
    def get_data_ingestion_config(self) -> Dict:
        config = self.config["data_ingestion"]

        # Create data_ingestion directories and files
        create_directories([config["root_dir"]])

        return config