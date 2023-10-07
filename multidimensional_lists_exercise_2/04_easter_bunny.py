def go_up(row, col, matrix):
    eggs = 0
    for row_index in range(row - 1, 0, -1):
        if matrix[row_index][col] != 'X':
            eggs += int(matrix[row_index][col])
        else:
            break
    return eggs


def go_down(row, col, matrix):
    eggs = 0
    for row_index in range(row + 1, len(matrix)):
        if matrix[row_index][col] != 'X':
            eggs += int(matrix[row_index][col])
        else:
            break
    return eggs


def go_left(row, col, matrix):
    eggs = 0
    for col_index in range(col):
        if matrix[row][col_index] != 'X':
            eggs += int(matrix[row][col_index])
        else:
            break
    return eggs


def go_right(row, col, matrix):
    eggs = 0
    for col_index in range(col + 1, len(matrix)):
        if matrix[row][col_index] != 'X':
            eggs += int(matrix[row][col_index])
        else:
            break
    return eggs



n = int(input())
start_row = 0
start_col = 0

matrix = []
for row in range(n):
    matrix.append(input().split())
    for col_index in range(n):
        if matrix[row][col_index] == 'B':
            start_row = row
            start_col = col_index
sum_up = go_up(start_row, start_col, matrix)
sum_down = go_down(start_row, start_col, matrix)
sum_left = go_left(start_row, start_col, matrix)
sum_right = go_right(start_row, start_col, matrix)

