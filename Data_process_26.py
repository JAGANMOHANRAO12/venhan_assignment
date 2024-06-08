import json
from typing import Dict, Any

def process_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    processed_data = {}
    if 'name' in data:
        processed_data['name'] = data['name']
    if 'age' in data:
        processed_data['age'] = data['age']
    if 'address' in data and 'city' in data['address']:
        processed_data['city'] = data['address']['city']

    return processed_data

json_file_path = 'example.json'
processed_data = process_json(json_file_path)
print(processed_data)
