rows = int(input())
matrix = [[int(el) for el in input().split(', ')]for row in range(rows)]

primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][(rows - i) - 1] for i in range(rows)]

# can also write the second_diagonal as matrix[i][-i -1]
# use negative index to got from the back forward

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
