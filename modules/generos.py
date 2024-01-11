import json
from utils.utils import load_json, save_json

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f)
