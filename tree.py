import os


def print_file(path_name):
    for file_name in os.listdir(path_name):
        path = os.path.join(path_name, file_name)
        return path


def writing_file(text):
    with open('directory.txt', 'w') as file:
        file.write(text)


if __name__ == '__main__':
    writing_file(print_file('.'))