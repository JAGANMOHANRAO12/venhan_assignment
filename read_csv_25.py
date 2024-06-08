import csv
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        return [row for row in csv_reader]

file_path = 'example.csv'
rows = read_csv(file_path)
for row in rows:
    print(row)
