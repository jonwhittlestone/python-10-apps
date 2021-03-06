import csv
import os

try:
    import statistics
except:
    import statistics_standin_for_py_2 as statistics

from data_types import Purchase


def print_header():
    print('--------- Data Mining Real Estate ----------')
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # with open(filename, 'r', encoding='utf-8') as fin:
    with open(filename, 'r') as fin:
        # Don't need to do this if we're using DictReader
        # header = fin.readline().strip()
        reader = csv.DictReader(fin, delimiter=',')
        purchases = []
        for row in reader:
            # print(type(row), row)
            p = Purchase.create_from_dict(row)
            purchases.append(p)

    # print(purchases[0].__dict__)
    return purchases


def query_data(data):
    data.sort(key=lambda p: p.price)
    # most expensive house?
    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths'.format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))

    # least expensive house?
    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths'.format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))

    # average house price?

    # This can be improved using list comprehensions
    # which can further be improved using generator expressions

    # prices = []
    # for pur in data:
    #     prices.append(pur.price)
    prices = [
        p.price  # project / or items
        for p in data  # the set to process
        ]

    ave_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(ave_price)))

    # average price of 2 bed houses
    two_bed_homes = (
        p  # project / or items
        for p in data  # the set to process
        if announce(p, "Average 2-bedrooms, found {}".format(p.beds[0])) and
        p.beds[0] == 2
    )

    ave_price = statistics.mean((p.price for p in two_bed_homes))
    ave_baths = statistics.mean((p.baths for p in two_bed_homes))

    print('The average home price for a 2 bed home is ${:,}. The average number of baths is {}'.format(
        int(ave_price), round(ave_baths)
    ))


def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


def main():
    print_header()
    filename = get_data_file()

    data = load_file(filename)
    query_data(data)


if __name__ == '__main__':
    main()
