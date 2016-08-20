import os

def load(name):
    """
    Creates and loads a new journal

    :param name: The base name of the journal to load
    :return: A new journal data structure populated with the file data
    """

    data = []

    # Todo. Populate from file if exists
    print('... loading file ...')
    filename = extract_full_filename(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    # Todo. Save file
    filename = extract_full_filename(name)
    print('... saving file to ... {}'. format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + "\n")


def extract_full_filename(name):
    return os.path.abspath(os.path.join('./journals/', name + '.jrl'))


def add_entry(text, journal_data):
    journal_data.append(text)