rows = int(input())

matrix = []

for row in range(rows):
    elements = list(input())
    matrix.append(elements)
position = None
symbol = input()
for row_index in range(rows):
    if position:
        break
    for column_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][column_index]
        if current_element == symbol:
            position = (row_index, column_index)
            print(position)
            break

if not position:
    print(f'{symbol} does not occur in the matrix')
