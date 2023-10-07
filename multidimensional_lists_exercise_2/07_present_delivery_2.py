presents = int(input())
n = int(input())

count_nice_kids = 0
Santa = ()
matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'S':
            Santa = (row, col)
            matrix[row][col] = '-'
        if matrix[row][col] == 'V':
            count_nice_kids += 1

# [print(*row) for row in matrix]
moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
nice_kids_with_presents = 0

while presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    curr_row = Santa[0] + moves[command][0]
    curr_col = Santa[1] + moves[command][1]

    if 0 <= curr_row <= n and 0 <= curr_col <= n:
        Santa = (curr_row, curr_col)

        if matrix[curr_row][curr_col] == '-':
            continue

        if matrix[curr_row][curr_col] == 'X':
            matrix[curr_row][curr_col] = '-'
            continue

        if matrix[curr_row][curr_col] == 'V':
            presents -= 1
            nice_kids_with_presents += 1
            count_nice_kids -= 1
            matrix[curr_row][curr_col] = '-'

        if matrix[curr_row][curr_col] == 'C':

            for move, index in moves.items():
                check_row = curr_row + index[0]
                check_col = curr_col + index[1]

                if matrix[check_row][check_col] == 'V':
                    presents -= 1
                    nice_kids_with_presents += 1
                    count_nice_kids -= 1
                    matrix[check_row][check_col] = '-'

                if matrix[check_row][check_col] == 'X':
                    presents -= 1
                    matrix[check_row][check_col] = '-'

if presents == 0:
    if count_nice_kids > 0:
        print("Santa ran out of presents!")

matrix[Santa[0]][Santa[1]] = 'S'
[print(*row) for row in matrix]

if count_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids} nice kid/s.")
