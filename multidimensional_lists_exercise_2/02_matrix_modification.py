def is_coordinate_valid(r, c, N):
    return 0 <= r < N and 0 <= c < N


n = int(input())
matrix = [[int(el) for el in input().split()] for row in range(n)]

# print(matrix)
while True:
    command = input().split()
    if command[0] == 'END':
        [print(*row) for row in matrix]
        break

    curr_row, curr_col, value = [int(x) for x in command[1:]]
    if command[0] == 'Add':
        if is_coordinate_valid(curr_row, curr_col, n):
            matrix[curr_row][curr_col] += value
        else:
            print('Invalid coordinates')
    if command[0] == 'Subtract':
        if is_coordinate_valid(curr_row, curr_col, n):
            matrix[curr_row][curr_col] -= value
        else:
            print('Invalid coordinates')
