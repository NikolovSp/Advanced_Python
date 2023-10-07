rows = int(input())

matrix = []
primary_diagonal = []
primary_diagonal_sum = 0
secondary_diagonal = []
secondary_diagonal_sum = 0

for row in range(rows):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)

for row_index in range(rows):
    primary_diagonal.append(matrix[row_index][row_index])
    primary_diagonal_sum += matrix[row_index][row_index]
    column_index = (len(matrix[row_index]) - row_index) - 1
    secondary_diagonal.append(matrix[row_index][column_index])
    secondary_diagonal_sum += matrix[row_index][column_index]

# print(f"Primary diagonal: sum = {'+ '.join([str(el) for el in primary_diagonal])} = {primary_diagonal_sum}")
total_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(total_difference)
