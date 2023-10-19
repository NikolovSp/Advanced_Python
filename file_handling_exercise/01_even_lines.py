import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, '01_text.txt')

symbols = ["-", ",", ".", "!", "?"]

with open(file_path, 'r') as file:
    result = []
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for char in symbols:
                line = line.replace(char, '@')
            result = line.split()
            print(' '.join(result[::-1]))
