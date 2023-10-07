rows, cols = [int(x) for x in input().split()]
matrix = [[int(el) for el in input().split()] for row in range(rows)]

max_sum = float('-inf')
max_row = 0
max_col = 0

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_sum = 0
        for sub_row in range(row_index, row_index + 3):
            for sub_col in range(col_index, col_index + 3):
                current_sum += matrix[sub_row][sub_col]

        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_col = col_index

print(f'Sum = {max_sum}')
max_submatrix = [matrix[row][max_col:max_col + 3] for row in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]
