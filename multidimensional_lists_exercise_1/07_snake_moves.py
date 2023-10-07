from collections import deque
rows, cols = [int(x) for x in input().split()]

snake = deque(input())
matrix = []

for row_index in range(rows):
    matrix.append([''] * cols)
    for col_index in range(cols):
        if row_index % 2 == 0:
            matrix[row_index][col_index] = snake[0]
        else:
            matrix[row_index][-1 - col_index] = snake[0]
        snake.rotate(-1)

[print(*row, sep='') for row in matrix]
