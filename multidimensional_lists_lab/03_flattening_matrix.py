rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split(',')])

# print(matrix)


flatten = []
for row in matrix:
    for el in row:
        flatten.append(el)
print(flatten)

flatten = []
flatten = [el for row in matrix for el in row]
print(flatten)

flatten = []
for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        flatten.append(matrix[row_index][col_index])
print(flatten)
