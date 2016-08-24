import os


def print_header():
    print('---------------------------------------------')
    print('--------    FILE SEARCH    ------------------')
    print('---------------------------------------------')

def get_folder_from_user():
    folder = input('What folder do you want to search? ')

    if not folder or not folder.strip():
       return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)

def get_search_text_from_user():
    text = input("What are you searching for? [single phrases only]" )
    return text

def search_folder(folder, text):
    print("Would search {} for {}" . format(folder, text))

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

    search_folder(folder, text)

if __name__ == '__main__':
    main()
