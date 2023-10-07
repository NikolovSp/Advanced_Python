matrix = []
current_position = ()
left_targets_counter = 0
for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'A':
            current_position = (row, col)
        if matrix[row][col] == 'x':
            left_targets_counter += 1

# print(matrix)
# print(starting_position)

n = int(input())
targets_shot = 0
targets_location = []
moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
training = False

for _ in range(n):
    command = input().split()

    if command[0] == 'shoot':
        row_index = current_position[0] + moves[command[1]][0]
        col_index = current_position[1] + moves[command[1]][1]

        while 0 <= row_index < 5 and 0 <= col_index < 5:

            if matrix[row_index][col_index] == '.':
                row_index += moves[command[1]][0]
                col_index += moves[command[1]][1]
                continue
            elif matrix[row_index][col_index] == 'x':
                targets_shot += 1
                targets_location.append([row_index, col_index])
                left_targets_counter -= 1
                matrix[row_index][col_index] = '.'
                break
    if left_targets_counter == 0:
        training = True
        break

    if command[0] == 'move':
        row_index = current_position[0] + moves[command[1]][0] * int(command[2])
        col_index = current_position[1] + moves[command[1]][1] * int(command[2])

        if 0 <= row_index < 5 and 0 <= col_index < 5 and matrix[row_index][col_index] == '.':
            current_position = (row_index, col_index)

if training:
    print(f"Training completed! All {targets_shot} targets hit.")
else:
    print(f"Training not completed! {left_targets_counter} targets left.")
[print(row) for row in targets_location]
