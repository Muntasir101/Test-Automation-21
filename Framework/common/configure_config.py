import json
import os


def load_config():
    config_file_path = os.path.join(os.getcwd(), 'Framework', 'Config', 'framework_config.json')
    with open(config_file_path, 'r') as file:
        config = json.load(file)

    return config
