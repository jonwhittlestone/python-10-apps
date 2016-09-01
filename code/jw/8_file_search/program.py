import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

def print_header():
    print('---------------------------------------------')
    print('--------    FILE SEARCH    ------------------')
    print('---------------------------------------------')

def get_folder_from_user():
    # /Users/jon/code/playground/python-10-apps/code/jw/8_file_search/books
    folder = input('What folder do you want to search? ')

    if not folder or not folder.strip():
       return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)

def get_search_text_from_user():
    text = input("What are you searching for? [single phrases only] ")
    return text.lower()


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='utf-8') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m

    # return matches

def search_folder(folder, text):
    # print("Would search {} for {}" . format(folder, text))
    # all_matches = []

    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)

        if item == '.DS_Store':
            continue

        if os.path.isdir(full_item):
            # added construct in Python 3.3. Loop through a set and hand them back one at a time
            # yield generator method means we only have a single line in
            # memory at atime
            yield from search_folder(full_item, text)
            # all_matches.extend(matches)
        else:
            yield from search_file(full_item, text)
            # all_matches.extend(matches)

    # return all_matches


def show_results(matches):
    match_count = 0
    for m in matches:
        print("** ----   MATCH   --- **")
        print()
        print('File: ' + m.file)
        print('Line #: {}' .format(m.line))
        print('Match: ' + m.text.strip())
        print()
        match_count += 1
    print('Found {} matches ..' . format(match_count))

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("Sorry, we can't search that text")
        return

    matches = search_folder(folder, text)
    show_results(matches)

if __name__ == '__main__':
    main()
