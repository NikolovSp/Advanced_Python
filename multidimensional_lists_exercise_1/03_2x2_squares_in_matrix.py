rows, cols = [int(x) for x in input().split()]

counter = 0
matrix = []
for row in range(rows):
    characters = input().split()
    matrix.append(characters)
# print(matrix)
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1]:
            if matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
                if matrix[row_index][col_index] == matrix[row_index + 1][col_index + 1]:
                    counter += 1

print(counter)
# be careful with index error... don't need to check the edge cases as they don't exist
