import os 
import json

def save_json(data):
    with open( 'w') as f:
        json.dump(data, f)

def load_json():
    if os.path.exists():
        with open('r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []