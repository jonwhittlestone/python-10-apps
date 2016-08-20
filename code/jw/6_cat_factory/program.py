import os
import cat_service
import subprocess

def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('----------------------------')
    print('---- CAT FACTORY -----------')


def get_or_create_output_folder():
    folder = 'cat_pictures'
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        os.mkdir(full_path)
        print('... created folder {}'.format(full_path))

    return full_path


def download_cats(folder):
    cat_count = 8
    print('Contacting Server ...')
    for i in range(0, cat_count):
        name = 'lolcat-{}' . format(i+1)
        print('Downloading cat ' + name)

        cat_service.get_cat(folder, name)

    print('Finished downloading all cats')


def display_cats(folder):
    print('Displaying cats in OSX')
    subprocess.call(['open', folder ])


if __name__ == '__main__':
    main()
