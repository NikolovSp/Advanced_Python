matrix = []

txt = input().split('|')

for row_index in range(len(txt)):
    matrix.append([int(x) for x in txt[-1 - row_index].split() if x != ' '])


for row_index in range(len(matrix)):
    print(*matrix[row_index], end=' ')
