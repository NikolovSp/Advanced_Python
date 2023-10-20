rows, cols = [int(x) for x in input().split(',')]
matrix = []

starting_position = ()
cheese_counter = 0
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "M":
            starting_position = (row, col)
            matrix[row][col] = "*"
        if matrix[row][col] == "C":
            cheese_counter += 1

# [print(''.join(row)) for row in matrix]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()
while command != "danger":
    current_row = starting_position[0] + directions[command][0]
    current_col = starting_position[1] + directions[command][1]

    if not 0 <= current_row < rows or not 0 <= current_col < cols:
        print("No more cheese for tonight!")
        break

    if matrix[current_row][current_col] == "T":
        print("Mouse is trapped!")
        starting_position = (current_row, current_col)
        break

    if matrix[current_row][current_col] == "@":
        command = input()
        continue

    if matrix[current_row][current_col] == "C":
        matrix[current_row][current_col] = "*"
        cheese_counter -= 1
        if cheese_counter == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            starting_position = (current_row, current_col)
            break

    starting_position = (current_row, current_col)
    command = input()
else:
    print("Mouse will come back later!")

matrix[starting_position[0]][starting_position[1]] = "M"

[print(''.join(row)) for row in matrix]
