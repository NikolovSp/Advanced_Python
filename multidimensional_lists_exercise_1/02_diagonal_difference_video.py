rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]
primary_diagonal = [matrix[row_index][row_index] for row_index in range(rows)]
secondary_diagonal = [matrix[row_index][rows - row_index - 1] for row_index in range(rows)]

results = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(results)
