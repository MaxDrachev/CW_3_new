import os.path

from config import ROOT_DIR
from src.utils import open_json, filter_operation, sort_operations, hide_number_from, hide_number_to, new_date

PATH_TO_FILE = os.path.join(ROOT_DIR, 'operations.json')


def main():
    operations_data = open_json(PATH_TO_FILE)
    operations = filter_operation(operations_data)
    operations = sort_operations(operations)
    for i in operations:
        print(f"{new_date(i)} {i['description']}")
        print(f"{hide_number_from(i)} -> {hide_number_to(i)}")
        print(f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n')


if __name__ == "__main__":
    main()
