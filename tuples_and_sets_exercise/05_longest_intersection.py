n = int(input())
longest_length = set()

for i in range(n):
    distances = input().split('-')
    first = distances[0]
    second = distances[1]
    start_a, end_a = [int(x) for x in first.split(',')]
    set_a = set(int(x) for x in range(start_a, end_a + 1))
    start_b, end_b = [int(x) for x in second.split(',')]
    range_b = range(start_b, end_b + 1)
# plus 1 in both cases in order to include the largest value in the set
    current_length = set_a.intersection(range_b)
    if len(current_length) > len(longest_length):
        longest_length = [int(x) for x in current_length]

# intersection can work with one set and range. However, if we use & both variables must be set
print(f'Longest intersection is {longest_length} with length {len(longest_length)}')
