n = int(input())
matrix = []

Alice = (0, 0)
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            Alice = (row, col)
            matrix[row][col] = '*'

party = True
moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
tea_collected = 0
row_index = Alice[0]
col_index = Alice[1]
while tea_collected < 10:
    direction = input()

    row_index += moves[direction][0]
    col_index += moves[direction][1]

    if not 0 <= row_index < n or not 0 <= col_index < n:
        party = False
        break

    if matrix[row_index][col_index] == "R":
        matrix[row_index][col_index] = '*'
        party = False
        break

    if matrix[row_index][col_index] == '.' or matrix[row_index][col_index] == '*':
        matrix[row_index][col_index] = '*'
        continue

    tea_collected += int(matrix[row_index][col_index])
    matrix[row_index][col_index] = '*'

if party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
