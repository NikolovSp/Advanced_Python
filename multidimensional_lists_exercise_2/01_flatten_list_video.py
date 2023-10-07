strings = input().split('|')
matrix = []
for row_index in range(len(strings) - 1, -1, -1):
    row = [int(x) for x in strings[row_index].split()]
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, sep=' ', end=' ')
