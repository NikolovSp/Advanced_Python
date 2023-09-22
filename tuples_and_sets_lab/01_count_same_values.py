numbers = tuple(map(float, input().split()))

# print(type(numbers))
# print(numbers)
times_seen = {}

for num in numbers:
    if num not in times_seen:
        times_seen[num] = 0
    times_seen[num] += 1

for key, value in times_seen.items():
    print(f'{key:.1f} - {value} times')
