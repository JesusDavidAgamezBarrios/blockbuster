import os
import json

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []
    
def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def get_id(data):
    if len(data) == 0:
        return 1
    else:
        return data[-1]["id"] + 1
    
def get_by_id(data, id):
    for item in data:
        if item["id"] == id:
            return item
    return None

def delete_by_id(data, id):
    for index, item in enumerate(data):
        if item["id"] == id:
            data.pop(index)
            return True
    return False

def update_by_id(data, id, new_item):
    for index, item in enumerate(data):
        if item["id"] == id:
            data[index] = new_item
            return True
    return False

def get_by_name(data, name):
    for item in data:
        if item["nombre"] == name:
            return item
    return None

def delete_by_name(data, name):
    for index, item in enumerate(data):
        if item["nombre"] == name:
            data.pop(index)
            return True
    return False

def update_by_name(data, name, new_item):
    for index, item in enumerate(data):
        if item["nombre"] == name:
            data[index] = new_item
            return True
    return False


