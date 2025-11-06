import csv
from typing import List, Dict


def read_csv_files(file_paths: List[str]) -> List[Dict[str, str]]:
    """
    Чтение нескольких CSV-файлов и возвращение списка словарей с данными.
    """
    all_data = []
    for file_path in file_paths:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            all_data.extend(list(reader))

    return all_data