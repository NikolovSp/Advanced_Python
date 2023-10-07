from sys import maxsize
n = int(input())
matrix = []
Bunny = (0, 0)

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'B':
            Bunny = (row, col)

# print(matrix)
# print(Bunny)
moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

max_eggs_collected = -maxsize
max_directions = []
max_move = ''
for direction, value in moves.items():
    row_index = Bunny[0] + value[0]
    col_index = Bunny[1] + value[1]
    current_eggs = 0
    current_directions = []
    while 0 <= row_index < n and 0 <= col_index < n:
        if matrix[row_index][col_index] == 'X':
            break
        current_eggs += int(matrix[row_index][col_index])
        current_directions.append([row_index, col_index])
        row_index += value[0]
        col_index += value[1]

    if current_eggs >= max_eggs_collected:
        max_eggs_collected = current_eggs
        max_move = direction
        max_directions = current_directions

print(max_move)
[print(row) for row in max_directions]
print(max_eggs_collected)
