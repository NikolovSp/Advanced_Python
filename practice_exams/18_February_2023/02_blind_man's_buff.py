rows, cols = [int(x) for x in input().split()]
start_position = ()
matrix = []
moves_counter = 0
opponents_touched = 0

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == 'B':
            start_position = (row, col)
# [print(row) for row in matrix]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()
    if command == 'Finish':
        break

    cur_row = start_position[0] + directions[command][0]
    cur_col = start_position[1] + directions[command][1]

    if not 0 <= cur_row < rows or not 0 <= cur_col < cols:
        continue

    if matrix[cur_row][cur_col] == 'O':
        continue

    if matrix[cur_row][cur_col] == 'P':
        opponents_touched += 1
        matrix[cur_row][cur_col] = '-'
        if opponents_touched == 3:
            moves_counter += 1
            break
    moves_counter += 1
    start_position = (cur_row, cur_col)

print('Game over!')
print(f'Touched opponents: {opponents_touched} Moves made: {moves_counter}')
