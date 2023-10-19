ROWS = 6
COLS = 7

direction_mapper = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
    (-1, 1),  # up right
    (1, -1),  # down left
    (-1, -1),  # up left
    (1, 1)  # down right
]


class FullColumn(Exception):
    pass


def print_matrix(mat):
    [print(row) for row in mat]


def is_column_valid(selected_column_index):
    return 0 <= selected_column_index < COLS


def place_player_number(col_i, mat, player_number):
    for row in range(ROWS - 1, -1, -1):
        if mat[row][col_i] == 0:
            mat[row][col_i] = player_number
            return row, col_i
    else:
        raise FullColumn


def is_valid_index(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return True
    return False


def requested_direction_count(current_row, current_col, row_movement, col_movement, curr_matrix, current_player):
    count = 1
    for i in range(1, 4):
        row_index_to_check = current_row + row_movement * i
        col_index_to_check = current_col + col_movement * i

        if not is_valid_index(row_index_to_check, col_index_to_check):
            break

        if curr_matrix[row_index_to_check][col_index_to_check] != current_player:
            break
        count += 1
    return count


def opposite_direction_count(current_row, current_col, row_movement, col_movement, curr_matrix, current_player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_movement * i
        col_index_to_check = current_col - col_movement * i

        if not is_valid_index(row_index_to_check, col_index_to_check):
            break

        if curr_matrix[row_index_to_check][col_index_to_check] != current_player:
            break
        count += 1
    return count


def is_winner(current_row, current_col, curr_matrix, current_player):
    for row_movement, col_movement in direction_mapper:
        count_direction = requested_direction_count(current_row, current_col, row_movement, col_movement, curr_matrix, current_player)
        opposite_direction = opposite_direction_count(current_row, current_col, row_movement, col_movement, curr_matrix, current_player)

        if count_direction + opposite_direction >= 4:
            return True
    return False


matrix = [[0 for col in range(COLS)] for row in range(ROWS)]
# [print(row) for row in matrix]
print_matrix(matrix)

player = 1
while True:
    try:
        column_index = int(input(f"Player {player} please select a column:")) - 1
        if not is_column_valid(column_index):
            raise ValueError
        row_index, col_index = place_player_number(column_index, matrix, player)

        if is_winner(row_index, col_index, matrix, player):
            print(f"Player {player} is winner!")
            print_matrix(matrix)
            break
        print_matrix(matrix)
    except ValueError:
        print(f"Player {player} please select a column between 1 and {COLS}:")
        continue
    except FullColumn:
        print(f"Player {player} the column is full , select another column:")

    player += 1
    if player % 2 == 0:
        player = 2
    else:
        player = 1
