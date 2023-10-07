n = int(input())
matrix = []
knights = []

for row_index in range(n):
    matrix.append([x for x in input()])
    for column_index in range(n):
        if matrix[row_index][column_index] == 'K':
            knights.append([row_index, column_index])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knights = [0, 0]
    for k_row, k_column in knights:
        curr_hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_col = k_column + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if matrix[new_row][new_col] == 'K':
                    curr_hits += 1
        if curr_hits > max_hits:
            max_hits = curr_hits
            max_knights = [k_row, k_column]

    if max_hits == 0:
#means there are no more knights to hit... end of the problem
        break
    else:
        knights.remove(max_knights)
        matrix[max_knights[0]][max_knights[1]] = '0'
        removed_knights += 1

print(removed_knights)
