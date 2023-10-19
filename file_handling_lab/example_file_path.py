import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
# adds the file directory to the closet current directory, considering the operating system
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'text.txt')

print(file_path)
