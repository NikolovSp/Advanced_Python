presents_available = int(input())
n = int(input())
curr_position = ()
matrix = []
nice_kids_counter = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            curr_position = (row, col)
            matrix[row][col] = '-'
        if matrix[row][col] == 'V':
            nice_kids_counter += 1

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
# print(matrix)
nice_kids_with_present = 0
command = input()
presents_given = 0
while command != 'Christmas morning' and presents_available > 0:
    row_index = curr_position[0] + moves[command][0]
    col_index = curr_position[1] + moves[command][1]

    if 0 <= row_index < n and 0 <= col_index < n:
        curr_position = (row_index, col_index)

        if matrix[row_index][col_index] == '-' or matrix[row_index][col_index] == 'X':
            command = input()

            continue

        if matrix[row_index][col_index] == 'V':
            presents_given += 1
            presents_available -= 1
            nice_kids_counter -= 1
            nice_kids_with_present += 1
            matrix[row_index][col_index] = '-'

        if matrix[row_index][col_index] == 'C':
            matrix[row_index][col_index] = '-'

            for direction in moves.items():
                row_index = curr_position[0] + direction[1][0]
                col_index = curr_position[1] + direction[1][1]
                matrix[row_index][col_index] = '-'
                if matrix[row_index][col_index] == 'V':
                    presents_given += 1
                    presents_available -= 1
                    nice_kids_counter -= 1
                    nice_kids_with_present += 1
                if matrix[row_index][col_index] == 'X':
                    presents_given += 1
                    presents_available -= 1

if nice_kids_counter > 0 and presents_available <= 0:
    print(f"Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))

if nice_kids_counter == 0:
    print(f'Good job, Santa! {nice_kids_with_present} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_counter} nice kid/s.')
