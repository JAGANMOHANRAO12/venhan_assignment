from typing import List

def write_file(file_path: str, lines: List[str]) -> None:
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')

# Example usage
lines_to_write = [
    "First line",
    "Second line",
    "Third line"
]

file_path = 'output.txt'
write_file(file_path, lines_to_write)
