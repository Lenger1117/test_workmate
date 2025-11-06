import argparse


def main():
    parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
    parser.add_argument('--files', nargs='+', required=True, help="Пути к CSV-файлам")
    parser.add_argument('--report', required=True, choices=, help="")
    args = parser.parse_args()