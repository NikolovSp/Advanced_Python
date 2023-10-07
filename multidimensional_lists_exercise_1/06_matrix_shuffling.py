rows, cols = [int(x) for x in input().split()]

matrix = []
for row_index in range(rows):
    nums = list(input().split())
    matrix.append(nums)
# print(matrix)

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if len(command) != 5:
        print("Invalid input!")
        continue
    if command[0] == 'swap':
        row_1 = int(command[1])
        col_1 = int(command[2])

        row_2 = int(command[3])
        col_2 = int(command[4])
        if row_1 < 0 or row_2 < 0 or col_1 < 0 or col_2 < 0:
            print("Invalid input!")
            continue
        if row_1 > rows or row_2 > rows or col_1 > cols or col_2 > cols:
            print("Invalid input!")
            continue
        x = matrix[row_1][col_1]
        y = matrix[row_2][col_2]
        matrix[row_1][col_1] = y
        matrix[row_2][col_2] = x

    else:
        print("Invalid input!")
        continue
    for row in matrix:
        print(' '.join(row))
