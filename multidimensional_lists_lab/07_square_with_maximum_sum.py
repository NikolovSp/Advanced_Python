rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(', ')]
    matrix.append(elements)
max_sum = float('-inf')
max_submatrix = []
# print(matrix)
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_bellow = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]
        sum_elements = current_element + next_element + element_bellow + diagonal_element

        if max_sum < sum_elements:
            max_sum = sum_elements
            max_submatrix = [
                [current_element, next_element],
                [element_bellow, diagonal_element]
            ]
print(*max_submatrix[0])
print(*max_submatrix[1])
print(max_sum)
