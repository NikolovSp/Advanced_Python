rows = int(input())
move_directions = input().split(', ')
start_position = ()
nuts_collected = 0
matrix = []
for row in range(rows):
    matrix.append(list(input()))
    for col in range(rows):
        if matrix[row][col] == 's':
            start_position = (row, col)

# [print(''.join(row)) for row in matrix]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for move in move_directions:
    curr_row = start_position[0] + directions[move][0]
    curr_col = start_position[1] + directions[move][1]
    if not 0 <= curr_row < rows or not 0 <= curr_col < rows:
        print('The squirrel is out of the field.')
        break

    if matrix[curr_row][curr_col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        break

    if matrix[curr_row][curr_col] == 'h':
        matrix[curr_row][curr_col] = '*'
        nuts_collected += 1
        if nuts_collected == 3:
            print('Good job! You have collected all hazelnuts!')
            break

    start_position = (curr_row, curr_col)
else:
    print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {nuts_collected}')
