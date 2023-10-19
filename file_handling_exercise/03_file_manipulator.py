import os

while True:
    line = input()
    if line == 'End':
        break

    command, filename, *extra = line.split('-')

    if command == 'Create':
        open(filename, 'w').close()

    elif command == 'Add':
        with open(filename, 'a') as file:
            file.write(f'{extra[0]}\n')

    elif command == 'Replace':
        try:
            with open(filename, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print('An error occurred')
        else:
            with open(filename, 'w') as new_file:
                text.replace(extra[0], extra[1])
                new_file.write(text)

    elif command == 'Delete':
        try:
            os.remove(filename)
        except OSError:
            print('An error occurred')
