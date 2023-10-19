from string import punctuation
import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, '02_text.txt')

with open(file_path, mode='r') as file:
    row_counter = 0
    for line in file:
        row_counter += 1
        letters = 0
        symbols = 0
        for char in line:
            if char.isalpha():
                letters += 1
            if char in punctuation:
                symbols += 1

        with open('02_output.txt', mode='a') as output:
            output.write(f'Line{row_counter}: {line[0:-1]} ({letters})({symbols})\n')

