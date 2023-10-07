rows = int(input())
matrix = [[int(el) for el in input().split()] for row in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break

    row, col, value = [int(x) for x in command[1:]]

    if row < 0 or row >= rows and col < 0 or col >= rows:
        print('Invalid coordinates')
        continue

    if command[0] == 'Add':
        matrix[row][col] += value
    elif command[0] == 'Subtract':
        matrix[row][col] -= value

[print(*row) for row in matrix]
