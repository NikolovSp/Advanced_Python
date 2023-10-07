def is_valid_location(row, col, N):
    return 0 <= row < N and 0 <= col < N


def is_knigt(row, col, matrix):
    return matrix[row][col] == 'K'


rows = int(input())
matrix = [[el for el in list(input())] for row in range(rows)]
# print(matrix)
removed_knigts_counter = 0

while True:
    max_attacks = 0
    row_max = 0
    col_max = 0
    for row_index in range(rows):
        for col_index in range(rows):
            attacks_counter = 0
            if matrix[row_index][col_index] == 'K':
                if is_valid_location(row_index - 2, col_index - 1, rows):
                    if is_knigt(row_index - 2, col_index - 1, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index - 2, col_index + 1, rows):
                    if is_knigt(row_index - 2, col_index + 1, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index - 1, col_index - 2, rows):
                    if is_knigt(row_index -1, col_index - 2, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index - 1, col_index + 2, rows):
                    if is_knigt(row_index - 1, col_index + 2, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index + 1, col_index - 2, rows):
                    if is_knigt(row_index + 1, col_index - 2, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index + 1, col_index + 2, rows):
                    if is_knigt(row_index + 1, col_index + 2, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index + 2, col_index - 1, rows):
                    if is_knigt(row_index + 2, col_index - 1, matrix):
                        attacks_counter += 1
                if is_valid_location(row_index + 2, col_index + 1, rows):
                    if is_knigt(row_index + 2, col_index + 1, matrix):
                        attacks_counter += 1

                if max_attacks < attacks_counter:
                    max_attacks = attacks_counter
                    row_max = row_index
                    col_max = col_index
    if max_attacks == 0:
        break
    else:
        matrix[row_max][col_max] = '0'
        removed_knigts_counter += 1

print(removed_knigts_counter)
