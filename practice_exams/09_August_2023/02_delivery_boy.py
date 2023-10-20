rows, cols = [int(x) for x in input().split()]

matrix = []
delivery_address = ()
start_position = ()
restaurant = ()
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'A':
            delivery_address = (row, col)
        if matrix[row][col] == 'B':
            start_position = (row, col)
            original_position = (row, col)
        if matrix[row][col] == 'P':
            restaurant = (row, col)
# [print(row) for row in matrix]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    row_index = start_position[0] + moves[command][0]
    col_index = start_position[1] + moves[command][1]

    if not 0 <= row_index < rows or not 0 <= col_index < cols:
        print("The delivery is late. Order is canceled.")
        matrix[original_position[0]][original_position[1]] = ' '
        break

    if matrix[row_index][col_index] == "A":
        matrix[row_index][col_index] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    if matrix[row_index][col_index] == "*":
        continue

    if matrix[row_index][col_index] == "-":
        matrix[row_index][col_index] = '.'

    if matrix[row_index][col_index] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[row_index][col_index] = "R"

    start_position = (row_index, col_index)

[print(''.join(row)) for row in matrix]
