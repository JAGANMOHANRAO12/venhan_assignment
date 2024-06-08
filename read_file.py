from typing import List

def read_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

file_path = 'example.txt'
lines = read_file(file_path)
for line in lines:
    print(line)
