import argparse
import sys
from tabulate import tabulate
from reporters import REPORT
from utils import read_csv_files


def main():
    parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
    parser.add_argument('--files', nargs='+', required=True, help="Пути к CSV-файлам")
    parser.add_argument('--report', required=True, choices=REPORT.keys(), help="")
    args = parser.parse_args()

    try:
        data = read_csv_files(args.files)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

    if not data:
        print("Файл не содержит данных.", file=sys.stderr)
        sys.exit(1)
    
    report_func = REPORT[args.report]
    report_data = report_func(data)

    if args.report == 'average-rating':
        enumerate_data = [
            (i, brand, rating)
            for i, (brand, rating) in enumerate(report_data, start=1)
        ]
        headers = ["", "brand", "rating"]
        table = tabulate(enumerate_data, headers=headers, tablefmt="grid", floatfmt=".2f")
        print(table)
    else:
        print(tabulate(report_data, tablefmt="grid"))


if __name__ == '__main__':
    main()