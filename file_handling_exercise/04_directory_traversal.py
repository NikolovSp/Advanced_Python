import os

files = {}
directory = './'

for element in os.listdir(directory):
    unknown = os.path.join(directory, element)
    if os.path.isfile(unknown):
        extension = element.split('.')[-1]
        if extension not in files:
            files[extension] = []
        files[extension].append(element)
    else:
        for direct_name in os.listdir(directory):
            filename = os.path.join(unknown, direct_name)
            if os.path.isfile(filename):
                ext = direct_name.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(filename)

with open(os.path.join(directory, 'report.txt'), 'w') as output:
    for ext, file_name in sorted(files.items()):
        output.write(f'.{ext}\n')
        for file in sorted(file_name):
            output.write(f'- - - {file}\n')
