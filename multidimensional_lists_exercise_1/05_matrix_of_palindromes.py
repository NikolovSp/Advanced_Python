rows, cols = [int(x) for x in input().split()]

matrix = []

for row_index in range(rows):
    matrix.append([])
    for col_index in range(cols):
        first_element = chr(row_index + 97)
        second_element = chr(row_index + col_index + 97)
        matrix[row_index].append(first_element + second_element + first_element)

for row in matrix:
    print(' '.join(row))
