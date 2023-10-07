rows, cols = [int(x) for x in input().split()]

start = ord('a')

for row_index in range(rows):
    for col_index in range(cols):
        print(f'{chr(start + row_index)}{chr(start + row_index + col_index)}{chr(start + row_index)}', end=' ')
    print()
