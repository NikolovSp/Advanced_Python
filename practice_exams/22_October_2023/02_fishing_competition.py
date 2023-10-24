rows = int(input())
start_position = ()
matrix = []
fish_collected = 0
start_row, start_col = 0, 0
for row in range(rows):
    matrix.append(list(input()))
    for col in range(rows):
        if matrix[row][col] == 'S':
            start_row, start_col = row, col
            matrix[row][col] = '-'
# [print(''.join(row)) for row in matrix]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
whirlpool = False
while True:
    command = input()
    if command == 'collect the nets':
        break

    curr_row = (start_row + directions[command][0]) % rows
    curr_col = (start_col + directions[command][1]) % rows

    if matrix[curr_row][curr_col] == 'W':
        print(f'You fell into a whirlpool! '
              f'The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: {f"[{curr_row},{curr_col}]"}')
        whirlpool = True
        exit()

    if matrix[curr_row][curr_col].isdigit():
        fish_collected += int(matrix[curr_row][curr_col])
        matrix[curr_row][curr_col] = '-'

    start_row, start_col = curr_row, curr_col

if fish_collected >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f" You need {20 - fish_collected} tons of fish more.")
if fish_collected > 0:
    print(f"Amount of fish caught: {fish_collected} tons.")
matrix[start_row][start_col] = 'S'
[print(''.join(row)) for row in matrix]
