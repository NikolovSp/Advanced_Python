rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([])
    elements = input()
    for element in elements:
        matrix[row].append(element)

# print(matrix)
char = input()
Found = False
for row in range(rows):
    for col in range(rows):
        if char == matrix[row][col]:
            print(f'({row}, {col})')
            Found = True
            break
    if Found:
        break
if not Found:
    print(f'{char} does not occur in the matrix')
