import csv
import os
from data_types import Purchase


def print_header():
    print('--------- Data Mining Real Estate ----------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # Don't need to do this if we're using DictReader
        # header = fin.readline().strip()
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    # print(purchases[0].__dict__)
    return purchases


def query_data(data):
    pass


def main():
    print_header()
    filename = get_data_file()

    data = load_file(filename)
    query_data(data)


if __name__ == '__main__':
    main()
