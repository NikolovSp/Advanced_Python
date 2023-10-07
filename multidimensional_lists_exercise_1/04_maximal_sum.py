from sys import maxsize

max_sum = -maxsize
rows, cols = [int(x) for x in input().split()]

matrix = []
for row in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)
# print(matrix)
#1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
submatrix = []
for row_index in range(rows - 2):
    sum_elements = 0
    for col_index in range(cols - 2):
        first_row_a = matrix[row_index][col_index]
        first_row_b = matrix[row_index][col_index + 1]
        first_row_c = matrix[row_index][col_index + 2]
        second_row_a = matrix[row_index + 1][col_index]
        second_row_b = matrix[row_index + 1][col_index + 1]
        second_row_c = matrix[row_index + 1][col_index + 2]
        third_row_a = matrix[row_index + 2][col_index]
        third_row_b = matrix[row_index + 2][col_index + 1]
        third_row_c = matrix[row_index + 2][col_index + 2]
        sum_elements = first_row_a + first_row_b + first_row_c + second_row_a + second_row_b + second_row_c + third_row_a + third_row_b + third_row_c

        if max_sum < sum_elements:
            max_sum = sum_elements
            submatrix = [
                [first_row_a, first_row_b, first_row_c],
                [second_row_a, second_row_b, second_row_c],
                [third_row_a, third_row_b, third_row_c]
            ]
print(f'Sum = {max_sum}')
print(*submatrix[0])
print(*submatrix[1])
print(*submatrix[2])

#watch the lecture to see a shorter way of solving this problem...
