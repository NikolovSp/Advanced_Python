rows = int(input())

matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(',')]
    matrix.append(elements)

# print(matrix)

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
primary_diagonal = []
primary_diagonal_sum = 0
secondary_diagonal = []
secondary_diagonal_sum = 0
for row_index in range(rows):
    primary_diagonal.append(matrix[row_index][row_index])
    primary_diagonal_sum += matrix[row_index][row_index]
    col_index = (len(matrix[row_index]) - row_index) - 1
    # works with rows (instead of len(matrix[rox_index]), because the matrix is square
    secondary_diagonal.append(matrix[row_index][col_index])
    secondary_diagonal_sum += (matrix[row_index][col_index])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {secondary_diagonal_sum}")
