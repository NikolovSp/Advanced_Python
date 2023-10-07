row, col = [int(x) for x in input().split(',')]

total_sum = 0
matrix = [[int(el) for el in input().split(', ')] for row_index in range(row)]
# for row_index in range(row):
#     elements = [int(el) for el in input().split(',')]
#     total_sum += sum(elements)
#     matrix.append(elements)
print(total_sum)
print(matrix)

