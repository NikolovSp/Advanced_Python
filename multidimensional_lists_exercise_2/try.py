moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
curr_row = 1
curr_col = 3

for move, index in moves.items():
    print(move, index)
    row = curr_row + index[0]
    col = curr_col + index[1]
    print(row, col)
