rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for row in range(rows):
    elements = [int(el) for el in input().split(' ')]
    matrix.append(elements)

# print(matrix)

for col in range(cols):
    sum_cols = 0
    for row in range(rows):
        sum_cols += matrix[row][col]
    print(sum_cols)
