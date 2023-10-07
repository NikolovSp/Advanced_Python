rows = int(input())
matrix = []
for row in range(rows):
    elements = [int(el) for el in input().split(' ')]
    matrix.append(elements)
# print(matrix)
sum_diagonal = 0
for row in range(rows):
    sum_diagonal += matrix[row][row]

print(sum_diagonal)
